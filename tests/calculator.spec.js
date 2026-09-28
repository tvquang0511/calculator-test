import { test, expect } from '@playwright/test';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const htmlUrl = `file://${path.resolve(__dirname, '../src/basicCalculator.html').replace(/\\/g, '/')}`;

test.describe('Basic Calculator - Prototype Baseline Suite', () => {

  test.beforeEach(async ({ page }) => {
    await page.goto(htmlUrl);
    await page.selectOption('#selectBuild', '0'); // Prototype
  });

  const waitForCalc = async (page) => {
    await page.waitForFunction(() => {
      const form = document.getElementById('calculatingForm');
      return form && form.hidden === true;
    }, { timeout: 3000 }).catch(() => {});
  };

  test('TC-UI-001: Kiểm tra tính khả dụng và hiển thị của các thành phần giao diện', async ({ page }) => {
    await expect(page.locator('#number1Field')).toBeVisible();
    await expect(page.locator('#number2Field')).toBeVisible();
    await expect(page.locator('#calculateButton')).toBeVisible();
    await expect(page.locator('#clearButton')).toBeEnabled();
  });

  test('TC-UI-002: Kiểm tra chức năng và trạng thái của Checkbox "Integers only"', async ({ page }) => {
    await page.fill('#number1Field', '5.8');
    await page.fill('#number2Field', '1');
    await page.selectOption('#selectOperationDropdown', '3');
    await page.check('#integerSelect');
    await page.click('#calculateButton');
    await waitForCalc(page);
    await expect(page.locator('#numberAnswerField')).toHaveValue('5');

    await page.uncheck('#integerSelect');
    await expect(page.locator('#numberAnswerField')).toHaveValue('5.8');
  });

  test('TC-UI-003: Kiểm tra chức năng nút "Clear" để reset giao diện', async ({ page }) => {
    await page.fill('#number1Field', '10');
    await page.fill('#number2Field', '20');
    await page.selectOption('#selectOperationDropdown', '0');
    await page.click('#calculateButton');
    await waitForCalc(page);
    await page.click('#clearButton');
    await expect(page.locator('#numberAnswerField')).toHaveValue('');
  });

  test('TC-MATH-001: Kiểm tra tính đúng đắn của phép tính cộng', async ({ page }) => {
    await page.fill('#number1Field', '10');
    await page.fill('#number2Field', '20');
    await page.selectOption('#selectOperationDropdown', '0');
    await page.click('#calculateButton');
    await waitForCalc(page);
    await expect(page.locator('#numberAnswerField')).toHaveValue('30');
  });

  test('TC-MATH-002: Kiểm tra phép tính trừ và thứ tự toán tử', async ({ page }) => {
    await page.fill('#number1Field', '15');
    await page.fill('#number2Field', '5');
    await page.selectOption('#selectOperationDropdown', '1');
    await page.click('#calculateButton');
    await waitForCalc(page);
    await expect(page.locator('#numberAnswerField')).toHaveValue('10');
  });

  test('TC-MATH-003: Kiểm tra phép tính chia ra kết quả số thập phân', async ({ page }) => {
    await page.fill('#number1Field', '7');
    await page.fill('#number2Field', '2');
    await page.selectOption('#selectOperationDropdown', '3');
    await page.click('#calculateButton');
    await waitForCalc(page);
    await expect(page.locator('#numberAnswerField')).toHaveValue('3.5');
  });

  test('TC-MATH-004: Kiểm tra xử lý ngoại lệ phép chia cho 0', async ({ page }) => {
    await page.fill('#number1Field', '10');
    await page.fill('#number2Field', '0');
    await page.selectOption('#selectOperationDropdown', '3');
    await page.click('#calculateButton');
    await waitForCalc(page);
    await expect(page.locator('#errorMsgField')).toHaveText('Divide by zero error!');
  });

  test('TC-MATH-005: Kiểm tra tính độc lập giữa các lần tính toán liên tiếp', async ({ page }) => {
    // Lần 1
    await page.fill('#number1Field', '2');
    await page.fill('#number2Field', '3');
    await page.selectOption('#selectOperationDropdown', '0');
    await page.click('#calculateButton');
    await waitForCalc(page);
    await expect(page.locator('#numberAnswerField')).toHaveValue('5');

    // Lần 2 (Nhập số mới mà không bấm Clear)
    await page.fill('#number1Field', '10');
    await page.fill('#number2Field', '20');
    await page.click('#calculateButton');
    await waitForCalc(page);
    await expect(page.locator('#numberAnswerField')).toHaveValue('30');
  });

  test('TC-STR-001: Kiểm tra chức năng ghép chuỗi văn bản', async ({ page }) => {
    await page.selectOption('#selectOperationDropdown', '4');
    await page.fill('#number1Field', 'Hello');
    await page.fill('#number2Field', 'World');
    await page.click('#calculateButton');
    await waitForCalc(page);
    await expect(page.locator('#numberAnswerField')).toHaveValue('HelloWorld');
  });

  test('TC-VAL-001: Bắt lỗi khi nhập ký tự không phải số trong phép toán số học', async ({ page }) => {
    await page.fill('#number1Field', 'abc');
    await page.fill('#number2Field', '10');
    await page.selectOption('#selectOperationDropdown', '0');
    await page.click('#calculateButton');
    await waitForCalc(page);
    await expect(page.locator('#errorMsgField')).toHaveText('Number 1 is not a number');
  });
});
