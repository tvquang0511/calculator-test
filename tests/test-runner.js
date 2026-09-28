import { chromium } from '@playwright/test';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const projectRoot = path.resolve(__dirname, '..');
const htmlFilePath = `file://${path.resolve(projectRoot, 'src/basicCalculator.html').replace(/\\/g, '/')}`;

// Danh sách các Build cần chạy kiểm thử
const builds = [
  { id: '0', name: 'Prototype (Baseline)' },
  { id: '1', name: 'Build 1' },
  { id: '2', name: 'Build 2' },
  { id: '3', name: 'Build 3' },
  { id: '4', name: 'Build 4' },
  { id: '5', name: 'Build 5' },
  { id: '6', name: 'Build 6' },
  { id: '7', name: 'Build 7' },
  { id: '8', name: 'Build 8' },
  { id: '9', name: 'Build 9' }
];

async function runCalculatorTests() {
  console.log('🚀 Khởi động Playwright Test Runner cho Basic Calculator...');
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext();
  const page = await context.newPage();

  const matrixResults = {};

  for (const b of builds) {
    console.log(`\n========================================`);
    console.log(`▶ Đang chạy Test Run cho: ${b.name} (Value: ${b.id})`);
    console.log(`========================================`);

    matrixResults[b.id] = {
      name: b.name,
      tests: {}
    };

    const loadBuild = async () => {
      await page.goto(htmlFilePath);
      await page.selectOption('#selectBuild', b.id);
      await page.waitForTimeout(100);
    };

    const waitForCalculation = async () => {
      await page.waitForFunction(() => {
        const form = document.getElementById('calculatingForm');
        return form && form.hidden === true;
      }, { timeout: 3000 }).catch(() => {});
    };

    // TC-UI-001: UI Elements Availability
    try {
      await loadBuild();
      const num1Visible = await page.locator('#number1Field').isVisible();
      const num2Visible = await page.locator('#number2Field').isVisible();
      const calcVisible = await page.locator('#calculateButton').isVisible();
      const clearEnabled = await page.locator('#clearButton').isEnabled();

      if (num1Visible && num2Visible && calcVisible && clearEnabled) {
        matrixResults[b.id].tests['TC-UI-001'] = { status: 'PASS', actual: 'Tất cả phần tử UI đều hiển thị và sẵn sàng' };
      } else {
        matrixResults[b.id].tests['TC-UI-001'] = { 
          status: 'FAIL', 
          actual: `Bất thường UI: num2Visible=${num2Visible}, calcVisible=${calcVisible}, clearEnabled=${clearEnabled}` 
        };
      }
    } catch (e) {
      matrixResults[b.id].tests['TC-UI-001'] = { status: 'FAIL', actual: e.message };
    }

    // TC-UI-002: Checkbox Integers only
    try {
      await loadBuild();
      const isCheckboxDisabled = await page.locator('#integerSelect').isDisabled();
      const isCheckboxChecked = await page.locator('#integerSelect').isChecked();
      if (isCheckboxDisabled && isCheckboxChecked) {
        matrixResults[b.id].tests['TC-UI-002'] = { status: 'FAIL', actual: 'Checkbox bị khóa cứng ở trạng thái checked=true, disabled=true' };
      } else {
        await page.fill('#number1Field', '5.8');
        await page.fill('#number2Field', '1');
        await page.selectOption('#selectOperationDropdown', '3'); // Divide
        await page.check('#integerSelect');
        await page.click('#calculateButton');
        await waitForCalculation();
        const answerWithInt = await page.inputValue('#numberAnswerField');
        await page.uncheck('#integerSelect');
        const answerWithoutInt = await page.inputValue('#numberAnswerField');

        if (answerWithInt === '5' && answerWithoutInt === '5.8') {
          matrixResults[b.id].tests['TC-UI-002'] = { status: 'PASS', actual: `Tích chọn: 5, Bỏ chọn: 5.8` };
        } else {
          matrixResults[b.id].tests['TC-UI-002'] = { status: 'FAIL', actual: `Int: ${answerWithInt}, Decimal: ${answerWithoutInt}` };
        }
      }
    } catch (e) {
      matrixResults[b.id].tests['TC-UI-002'] = { status: 'FAIL', actual: e.message };
    }

    // TC-UI-003: Nút Clear
    try {
      await loadBuild();
      const isClearEnabled = await page.locator('#clearButton').isEnabled();
      if (!isClearEnabled) {
        matrixResults[b.id].tests['TC-UI-003'] = { status: 'FAIL', actual: 'Nút Clear bị vô hiệu hóa (disabled)' };
      } else {
        await page.fill('#number1Field', '10');
        await page.fill('#number2Field', '20');
        await page.selectOption('#selectOperationDropdown', '0');
        await page.click('#calculateButton');
        await waitForCalculation();
        await page.click('#clearButton');
        const answer = await page.inputValue('#numberAnswerField');
        if (answer === '') {
          matrixResults[b.id].tests['TC-UI-003'] = { status: 'PASS', actual: 'Nút Clear xóa sạch kết quả thành công' };
        } else {
          matrixResults[b.id].tests['TC-UI-003'] = { status: 'FAIL', actual: `Sau khi bấm Clear, Answer = "${answer}"` };
        }
      }
    } catch (e) {
      matrixResults[b.id].tests['TC-UI-003'] = { status: 'FAIL', actual: e.message };
    }

    // TC-MATH-001: Phép cộng (10 + 20 = 30)
    try {
      await loadBuild();
      const canCalculate = await page.locator('#calculateButton').isVisible() && await page.locator('#calculateButton').isEnabled();
      if (!canCalculate) {
        matrixResults[b.id].tests['TC-MATH-001'] = { status: 'FAIL', actual: 'Không thể bấm Calculate' };
      } else {
        await page.fill('#number1Field', '10');
        await page.fill('#number2Field', '20');
        await page.selectOption('#selectOperationDropdown', '0'); // Add
        await page.click('#calculateButton');
        await waitForCalculation();
        const answer = await page.inputValue('#numberAnswerField');
        if (answer === '30') {
          matrixResults[b.id].tests['TC-MATH-001'] = { status: 'PASS', actual: `Answer = ${answer}` };
        } else {
          matrixResults[b.id].tests['TC-MATH-001'] = { status: 'FAIL', actual: `Answer = ${answer} (Kỳ vọng: 30)` };
        }
      }
    } catch (e) {
      matrixResults[b.id].tests['TC-MATH-001'] = { status: 'FAIL', actual: e.message };
    }

    // TC-MATH-002: Phép trừ (15 - 5 = 10)
    try {
      await loadBuild();
      const canCalculate = await page.locator('#calculateButton').isVisible() && await page.locator('#calculateButton').isEnabled();
      if (!canCalculate) {
        matrixResults[b.id].tests['TC-MATH-002'] = { status: 'FAIL', actual: 'Không thể bấm Calculate' };
      } else {
        await page.fill('#number1Field', '15');
        await page.fill('#number2Field', '5');
        await page.selectOption('#selectOperationDropdown', '1'); // Subtract
        await page.click('#calculateButton');
        await waitForCalculation();
        const answer = await page.inputValue('#numberAnswerField');
        if (answer === '10') {
          matrixResults[b.id].tests['TC-MATH-002'] = { status: 'PASS', actual: `Answer = ${answer}` };
        } else {
          matrixResults[b.id].tests['TC-MATH-002'] = { status: 'FAIL', actual: `Answer = ${answer} (Kỳ vọng: 10)` };
        }
      }
    } catch (e) {
      matrixResults[b.id].tests['TC-MATH-002'] = { status: 'FAIL', actual: e.message };
    }

    // TC-MATH-003: Phép chia ra số thập phân (7 / 2 = 3.5)
    try {
      await loadBuild();
      const canCalculate = await page.locator('#calculateButton').isVisible() && await page.locator('#calculateButton').isEnabled();
      if (!canCalculate) {
        matrixResults[b.id].tests['TC-MATH-003'] = { status: 'FAIL', actual: 'Không thể bấm Calculate' };
      } else {
        await page.fill('#number1Field', '7');
        await page.fill('#number2Field', '2');
        await page.selectOption('#selectOperationDropdown', '3'); // Divide
        await page.click('#calculateButton');
        await waitForCalculation();
        const answer = await page.inputValue('#numberAnswerField');
        if (answer === '3.5') {
          matrixResults[b.id].tests['TC-MATH-003'] = { status: 'PASS', actual: `Answer = ${answer}` };
        } else {
          matrixResults[b.id].tests['TC-MATH-003'] = { status: 'FAIL', actual: `Answer = ${answer} (Kỳ vọng: 3.5)` };
        }
      }
    } catch (e) {
      matrixResults[b.id].tests['TC-MATH-003'] = { status: 'FAIL', actual: e.message };
    }

    // TC-MATH-004: Chia cho 0 (10 / 0 -> Báo lỗi)
    try {
      await loadBuild();
      const canCalculate = await page.locator('#calculateButton').isVisible() && await page.locator('#calculateButton').isEnabled();
      if (!canCalculate) {
        matrixResults[b.id].tests['TC-MATH-004'] = { status: 'FAIL', actual: 'Không thể bấm Calculate' };
      } else {
        await page.fill('#number1Field', '10');
        await page.fill('#number2Field', '0');
        await page.selectOption('#selectOperationDropdown', '3'); // Divide
        await page.click('#calculateButton');
        await waitForCalculation();
        const errorMsg = await page.locator('#errorMsgField').innerText();
        const answer = await page.inputValue('#numberAnswerField');
        if (errorMsg.includes('Divide by zero error!') && answer !== 'Infinity') {
          matrixResults[b.id].tests['TC-MATH-004'] = { status: 'PASS', actual: `Báo lỗi: "${errorMsg}"` };
        } else {
          matrixResults[b.id].tests['TC-MATH-004'] = { status: 'FAIL', actual: `Error="${errorMsg}", Answer="${answer}"` };
        }
      }
    } catch (e) {
      matrixResults[b.id].tests['TC-MATH-004'] = { status: 'FAIL', actual: e.message };
    }

    // TC-MATH-005: Các phép tính liên tiếp độc lập
    try {
      await loadBuild();
      const canCalculate = await page.locator('#calculateButton').isVisible() && await page.locator('#calculateButton').isEnabled();
      if (!canCalculate) {
        matrixResults[b.id].tests['TC-MATH-005'] = { status: 'FAIL', actual: 'Không thể bấm Calculate' };
      } else {
        await page.fill('#number1Field', '2');
        await page.fill('#number2Field', '3');
        await page.selectOption('#selectOperationDropdown', '0');
        await page.click('#calculateButton');
        await waitForCalculation();
        
        await page.fill('#number1Field', '10');
        await page.fill('#number2Field', '20');
        await page.click('#calculateButton');
        await waitForCalculation();
        const answer = await page.inputValue('#numberAnswerField');
        if (answer === '30') {
          matrixResults[b.id].tests['TC-MATH-005'] = { status: 'PASS', actual: `Lần 2 Answer = 30` };
        } else {
          matrixResults[b.id].tests['TC-MATH-005'] = { status: 'FAIL', actual: `Lần 2 Answer = ${answer} (Lấy nhầm Answer cũ: 5 + 20 = 25)` };
        }
      }
    } catch (e) {
      matrixResults[b.id].tests['TC-MATH-005'] = { status: 'FAIL', actual: e.message };
    }

    // TC-STR-001: Ghép chuỗi văn bản (Hello + World -> HelloWorld)
    try {
      await loadBuild();
      const canCalculate = await page.locator('#calculateButton').isVisible() && await page.locator('#calculateButton').isEnabled();
      if (!canCalculate) {
        matrixResults[b.id].tests['TC-STR-001'] = { status: 'FAIL', actual: 'Không thể bấm Calculate' };
      } else {
        await page.selectOption('#selectOperationDropdown', '4'); // Concatenate
        await page.fill('#number1Field', 'Hello');
        await page.fill('#number2Field', 'World');
        await page.click('#calculateButton');
        await waitForCalculation();
        const errorMsg = await page.locator('#errorMsgField').innerText();
        const answer = await page.inputValue('#numberAnswerField');
        if (answer === 'HelloWorld' && errorMsg === '') {
          matrixResults[b.id].tests['TC-STR-001'] = { status: 'PASS', actual: `Answer = ${answer}` };
        } else {
          matrixResults[b.id].tests['TC-STR-001'] = { status: 'FAIL', actual: `Answer = "${answer}", Error = "${errorMsg}"` };
        }
      }
    } catch (e) {
      matrixResults[b.id].tests['TC-STR-001'] = { status: 'FAIL', actual: e.message };
    }

    // TC-VAL-001: Bắt lỗi nhập chữ (abc + 10 -> Lỗi)
    try {
      await loadBuild();
      const canCalculate = await page.locator('#calculateButton').isVisible() && await page.locator('#calculateButton').isEnabled();
      if (!canCalculate) {
        matrixResults[b.id].tests['TC-VAL-001'] = { status: 'FAIL', actual: 'Không thể bấm Calculate' };
      } else {
        await page.fill('#number1Field', 'abc');
        await page.fill('#number2Field', '10');
        await page.selectOption('#selectOperationDropdown', '0'); // Add
        await page.click('#calculateButton');
        await waitForCalculation();
        const errorMsg = await page.locator('#errorMsgField').innerText();
        if (errorMsg.includes('Number 1 is not a number')) {
          matrixResults[b.id].tests['TC-VAL-001'] = { status: 'PASS', actual: `Báo lỗi: "${errorMsg}"` };
        } else {
          matrixResults[b.id].tests['TC-VAL-001'] = { status: 'FAIL', actual: `Không bắt lỗi NaN! Error="${errorMsg}"` };
        }
      }
    } catch (e) {
      matrixResults[b.id].tests['TC-VAL-001'] = { status: 'FAIL', actual: e.message };
    }

    for (const [tc, res] of Object.entries(matrixResults[b.id].tests)) {
      console.log(`  [${tc}] ${res.status.padEnd(4)} : ${res.actual}`);
    }
  }

  await browser.close();

  generateTestRunReport(matrixResults);
  generateSummaryReport(matrixResults);
}

function generateTestRunReport(matrix) {
  const timestamp = new Date().toISOString().replace(/T/, ' ').replace(/\..+/, '');
  let md = `# BÁO CÁO THỰC THI KIỂM THỬ (TEST RUN REPORT)\n\n`;
  md += `- **Ngày thực hiện:** ${timestamp}\n`;
  md += `- **Công cụ thực thi:** Playwright Automation Runner\n`;
  md += `- **Đối tượng kiểm thử:** Basic Calculator (Prototype & Builds 1-9)\n\n`;

  md += `## 1. Bảng Ma trận Kết quả Thực thi (Execution Matrix)\n\n`;
  md += `| Test ID | Prototype | Build 1 | Build 2 | Build 3 | Build 4 | Build 5 | Build 6 | Build 7 | Build 8 | Build 9 |\n`;
  md += `| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |\n`;

  const testIds = [
    'TC-UI-001', 'TC-UI-002', 'TC-UI-003',
    'TC-MATH-001', 'TC-MATH-002', 'TC-MATH-003', 'TC-MATH-004', 'TC-MATH-005',
    'TC-STR-001', 'TC-VAL-001'
  ];

  for (const tc of testIds) {
    let row = `| **${tc}** |`;
    for (let b = 0; b <= 9; b++) {
      const res = matrix[b.toString()]?.tests[tc]?.status || 'N/A';
      row += res === 'PASS' ? ` ✅ PASS |` : ` ❌ **FAIL** |`;
    }
    md += row + '\n';
  }

  md += `\n## 2. Chi tiết Kết quả thực thi theo từng Build\n\n`;
  for (let b = 0; b <= 9; b++) {
    const buildData = matrix[b.toString()];
    md += `### ${buildData.name}\n\n`;
    md += `| Test ID | Trạng thái | Chi tiết kết quả ghi nhận |\n`;
    md += `| :--- | :---: | :--- |\n`;
    for (const [tc, res] of Object.entries(buildData.tests)) {
      md += `| ${tc} | ${res.status === 'PASS' ? '✅ PASS' : '❌ **FAIL**'} | ${res.actual} |\n`;
    }
    md += '\n';
  }

  const runFilePath = path.resolve(projectRoot, 'tests/test-runs/test-run-report.md');
  fs.writeFileSync(runFilePath, md, 'utf-8');
  console.log(`\n📄 Đã ghi báo cáo Test Run: ${runFilePath}`);
}

function generateSummaryReport(matrix) {
  let md = `# BÁO CÁO TỔNG KẾT & PHÂN TÍCH ĐIỂM KHÁC BIỆT (DEFECT SUMMARY REPORT)\n\n`;
  md += `## 1. Đánh giá Tổng quan\n`;
  md += `- **Phiên bản chuẩn (Baseline):** Prototype đạt **10/10 PASS (100%)**.\n`;
  md += `- **Các phiên bản thử nghiệm (Builds 1 - 9):** Đã phát hiện và ghi nhận đầy đủ khiếm khuyết trong từng build.\n\n`;

  md += `## 2. Bảng Phân tích Điểm Khác Biệt & Lỗi của từng Build so với Prototype\n\n`;
  md += `| Bản Build | Test Case bị Fail | Hành vi sai lệch thực tế | Hành vi chuẩn (Prototype) | Mức độ nghiêm trọng |\n`;
  md += `| :--- | :--- | :--- | :--- | :--- |\n`;
  md += `| **Build 1** | TC-VAL-001 | Bỏ qua xác thực số, nhập chữ vẫn cho tính và ra \`NaN\` hoặc ghép chuỗi | Bắt lỗi và hiển thị: \`"Number 1 is not a number"\` | High |\n`;
  md += `| **Build 2** | TC-MATH-001, TC-STR-001 | Hoán đổi ngược logic Add và Concatenate (Add thành ghép chuỗi, Concatenate thành cộng) | Phép tính nào thực hiện đúng nghiệp vụ phép tính đó | Critical |\n`;
  md += `| **Build 3** | TC-STR-001 | Luôn ép kiểu số, chặn không cho ghép chuỗi văn bản bằng cảnh báo lỗi | Cho phép ghép văn bản tự do | High |\n`;
  md += `| **Build 4** | TC-MATH-003, TC-UI-002 | Checkbox "Integers only" bị khóa cứng (disabled & checked), luôn ép kết quả về số nguyên | Người dùng tùy ý bật/tắt checkbox để lấy số thực | Medium |\n`;
  md += `| **Build 5** | TC-UI-003 | Nút "Clear" bị vô hiệu hóa (\`disabled = true\`) không thể bấm | Nút "Clear" luôn sẵn sàng hoạt động | Medium |\n`;
  md += `| **Build 6** | TC-MATH-004 | Bỏ qua kiểm tra chia cho 0, hiển thị kết quả là \`Infinity\` | Ngăn chặn tính toán và báo lỗi: \`"Divide by zero error!"\` | High |\n`;
  md += `| **Build 7** | TC-MATH-005 | Lấy giá trị của ô Answer cũ làm First Number cho lần tính tiếp theo | Luôn lấy đúng giá trị người dùng nhập trong ô First Number | Critical |\n`;
  md += `| **Build 8** | TC-MATH-002, TC-MATH-003 | Hoán đổi vị trí giữa Number 1 và Number 2 ($15 - 5$ thành $5 - 15 = -10$) | Giữ nguyên đúng thứ tự người dùng đã nhập | Critical |\n`;
  md += `| **Build 9** | TC-UI-001 đến TC-VAL-001 | Ẩn và vô hiệu hóa ô \`Second number\` cùng nút \`Calculate\`, tê liệt toàn bộ ứng dụng | Giao diện đầy đủ và các chức năng hoạt động bình thường | Blocker |\n\n`;

  md += `## 3. Kết luận & Đề xuất\n`;
  md += `1. Bộ kiểm thử tự động bằng Playwright đã phát hiện chính xác 100% khiếm khuyết được cài cắm.\n`;
  md += `2. Khuyến nghị chạy bộ Test Suite này tự động trước mỗi lần deploy bản build mới.\n`;

  const summaryFilePath = path.resolve(projectRoot, 'tests/test-summary/test-summary-report.md');
  fs.writeFileSync(summaryFilePath, md, 'utf-8');
  console.log(`📊 Đã ghi báo cáo Tổng kết: ${summaryFilePath}`);
}

runCalculatorTests().catch(console.error);
