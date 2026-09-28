import { test, expect } from '@playwright/test';
import { CalculatorPage } from './pages/CalculatorPage.js';

test.describe('Basic Calculator Automation Suite - 80 Test Cases', () => {
  /** @type {CalculatorPage} */
  let calc;

  test.beforeEach(async ({ page }) => {
    calc = new CalculatorPage(page);
    await calc.goto();
  });

  // =========================================================================
  // TS-001: ADDITION (TC-001 -> TC-011)
  // =========================================================================
  test.describe('TS-001: Addition', () => {
    test('TC-001: Phép cộng hai số nguyên dương (25 + 15 = 40)', async () => {
      await calc.performCalculation({ number1: '25', number2: '15', operation: 'Add', integersOnly: false });
      expect(await calc.getAnswer()).toBe('40');
      expect(await calc.getErrorMessage()).toBe('');
    });

    test('TC-002: Phép cộng số dương và số âm (50 + (-20) = 30)', async () => {
      await calc.performCalculation({ number1: '50', number2: '-20', operation: 'Add', integersOnly: false });
      expect(await calc.getAnswer()).toBe('30');
    });

    test('TC-003: Phép cộng số âm và số dương (-35 + 10 = -25)', async () => {
      await calc.performCalculation({ number1: '-35', number2: '10', operation: 'Add', integersOnly: false });
      expect(await calc.getAnswer()).toBe('-25');
    });

    test('TC-004: Phép cộng hai số nguyên âm (-12 + (-18) = -30)', async () => {
      await calc.performCalculation({ number1: '-12', number2: '-18', operation: 'Add', integersOnly: false });
      expect(await calc.getAnswer()).toBe('-30');
    });

    test('TC-005: Phép cộng số 0 với một số dương (0 + 42 = 42)', async () => {
      await calc.performCalculation({ number1: '0', number2: '42', operation: 'Add', integersOnly: false });
      expect(await calc.getAnswer()).toBe('42');
    });

    test('TC-006: Phép cộng một số với số 0 (88 + 0 = 88)', async () => {
      await calc.performCalculation({ number1: '88', number2: '0', operation: 'Add', integersOnly: false });
      expect(await calc.getAnswer()).toBe('88');
    });

    test('TC-007: Phép cộng 0 + 0 = 0', async () => {
      await calc.performCalculation({ number1: '0', number2: '0', operation: 'Add', integersOnly: false });
      expect(await calc.getAnswer()).toBe('0');
    });

    test('TC-008: Phép cộng hai số thập phân (12.35 + 7.42 = 19.77)', async () => {
      await calc.performCalculation({ number1: '12.35', number2: '7.42', operation: 'Add', integersOnly: false });
      expect(await calc.getAnswer()).toBe('19.77');
    });

    test('TC-009: Phép cộng số thập phân với số nguyên (8.75 + 11 = 19.75)', async () => {
      await calc.performCalculation({ number1: '8.75', number2: '11', operation: 'Add', integersOnly: false });
      expect(await calc.getAnswer()).toBe('19.75');
    });

    test('TC-010: Phép cộng hai số thập phân âm (-4.5 + (-3.2) = -7.7)', async () => {
      await calc.performCalculation({ number1: '-4.5', number2: '-3.2', operation: 'Add', integersOnly: false });
      expect(await calc.getAnswer()).toBe('-7.7');
    });

    test('TC-011: Phép cộng hai số nguyên lớn 9 chữ số', async () => {
      await calc.performCalculation({ number1: '500000000', number2: '400000000', operation: 'Add', integersOnly: false });
      expect(await calc.getAnswer()).toBe('900000000');
    });
  });

  // =========================================================================
  // TS-002: SUBTRACTION (TC-012 -> TC-021)
  // =========================================================================
  test.describe('TS-002: Subtraction', () => {
    test('TC-012: Phép trừ hai số nguyên dương kết quả dương (45 - 20 = 25)', async () => {
      await calc.performCalculation({ number1: '45', number2: '20', operation: 'Subtract', integersOnly: false });
      expect(await calc.getAnswer()).toBe('25');
    });

    test('TC-013: Phép trừ hai số nguyên dương kết quả âm (15 - 40 = -25)', async () => {
      await calc.performCalculation({ number1: '15', number2: '40', operation: 'Subtract', integersOnly: false });
      expect(await calc.getAnswer()).toBe('-25');
    });

    test('TC-014: Phép trừ hai số giống nhau kết quả 0 (99 - 99 = 0)', async () => {
      await calc.performCalculation({ number1: '99', number2: '99', operation: 'Subtract', integersOnly: false });
      expect(await calc.getAnswer()).toBe('0');
    });

    test('TC-015: Phép trừ số dương cho số âm (30 - (-15) = 45)', async () => {
      await calc.performCalculation({ number1: '30', number2: '-15', operation: 'Subtract', integersOnly: false });
      expect(await calc.getAnswer()).toBe('45');
    });

    test('TC-016: Phép trừ số âm cho số dương (-20 - 30 = -50)', async () => {
      await calc.performCalculation({ number1: '-20', number2: '30', operation: 'Subtract', integersOnly: false });
      expect(await calc.getAnswer()).toBe('-50');
    });

    test('TC-017: Phép trừ hai số âm (-10 - (-25) = 15)', async () => {
      await calc.performCalculation({ number1: '-10', number2: '-25', operation: 'Subtract', integersOnly: false });
      expect(await calc.getAnswer()).toBe('15');
    });

    test('TC-018: Phép trừ hai số thập phân (15.8 - 4.3 = 11.5)', async () => {
      await calc.performCalculation({ number1: '15.8', number2: '4.3', operation: 'Subtract', integersOnly: false });
      expect(await calc.getAnswer()).toBe('11.5');
    });

    test('TC-019: Phép trừ với số thập phân âm (-5.75 - 2.25 = -8)', async () => {
      await calc.performCalculation({ number1: '-5.75', number2: '2.25', operation: 'Subtract', integersOnly: false });
      expect(await calc.getAnswer()).toBe('-8');
    });

    test('TC-020: Phép trừ số 0 cho một số dương (0 - 67 = -67)', async () => {
      await calc.performCalculation({ number1: '0', number2: '67', operation: 'Subtract', integersOnly: false });
      expect(await calc.getAnswer()).toBe('-67');
    });

    test('TC-021: Phép trừ hai số lớn (99999999 - 11111111 = 88888888)', async () => {
      await calc.performCalculation({ number1: '99999999', number2: '11111111', operation: 'Subtract', integersOnly: false });
      expect(await calc.getAnswer()).toBe('88888888');
    });
  });

  // =========================================================================
  // TS-003: MULTIPLICATION (TC-022 -> TC-030)
  // =========================================================================
  test.describe('TS-003: Multiplication', () => {
    test('TC-022: Phép nhân hai số nguyên dương (6 * 7 = 42)', async () => {
      await calc.performCalculation({ number1: '6', number2: '7', operation: 'Multiply', integersOnly: false });
      expect(await calc.getAnswer()).toBe('42');
    });

    test('TC-023: Phép nhân số dương với số âm (8 * (-5) = -40)', async () => {
      await calc.performCalculation({ number1: '8', number2: '-5', operation: 'Multiply', integersOnly: false });
      expect(await calc.getAnswer()).toBe('-40');
    });

    test('TC-024: Phép nhân hai số nguyên âm (-9 * (-4) = 36)', async () => {
      await calc.performCalculation({ number1: '-9', number2: '-4', operation: 'Multiply', integersOnly: false });
      expect(await calc.getAnswer()).toBe('36');
    });

    test('TC-025: Phép nhân một số với 0 (123 * 0 = 0)', async () => {
      await calc.performCalculation({ number1: '123', number2: '0', operation: 'Multiply', integersOnly: false });
      expect(await calc.getAnswer()).toBe('0');
    });

    test('TC-026: Phép nhân 0 với một số (0 * (-78) = 0)', async () => {
      await calc.performCalculation({ number1: '0', number2: '-78', operation: 'Multiply', integersOnly: false });
      expect(Number(await calc.getAnswer())).toBe(0);
    });

    test('TC-027: Phép nhân một số với 1 (56 * 1 = 56)', async () => {
      await calc.performCalculation({ number1: '56', number2: '1', operation: 'Multiply', integersOnly: false });
      expect(await calc.getAnswer()).toBe('56');
    });

    test('TC-028: Phép nhân một số với -1 (89 * (-1) = -89)', async () => {
      await calc.performCalculation({ number1: '89', number2: '-1', operation: 'Multiply', integersOnly: false });
      expect(await calc.getAnswer()).toBe('-89');
    });

    test('TC-029: Phép nhân hai số thập phân (2.5 * 1.5 = 3.75)', async () => {
      await calc.performCalculation({ number1: '2.5', number2: '1.5', operation: 'Multiply', integersOnly: false });
      expect(await calc.getAnswer()).toBe('3.75');
    });

    test('TC-030: Phép nhân hai số lớn (100000 * 100000 = 10000000000)', async () => {
      await calc.performCalculation({ number1: '100000', number2: '100000', operation: 'Multiply', integersOnly: false });
      expect(await calc.getAnswer()).toBe('10000000000');
    });
  });

  // =========================================================================
  // TS-004: DIVISION (TC-031 -> TC-040)
  // =========================================================================
  test.describe('TS-004: Division', () => {
    test('TC-031: Phép chia hết hai số nguyên dương (20 / 4 = 5)', async () => {
      await calc.performCalculation({ number1: '20', number2: '4', operation: 'Divide', integersOnly: false });
      expect(await calc.getAnswer()).toBe('5');
    });

    test('TC-032: Phép chia có phần dư hữu hạn (5 / 2 = 2.5)', async () => {
      await calc.performCalculation({ number1: '5', number2: '2', operation: 'Divide', integersOnly: false });
      expect(await calc.getAnswer()).toBe('2.5');
    });

    test('TC-033: Phép chia có phần dư vô hạn tuần hoàn (10 / 3)', async () => {
      await calc.performCalculation({ number1: '10', number2: '3', operation: 'Divide', integersOnly: false });
      expect(await calc.getAnswer()).toContain('3.33333333333333');
    });

    test('TC-034: Phép chia số dương cho số âm (18 / (-3) = -6)', async () => {
      await calc.performCalculation({ number1: '18', number2: '-3', operation: 'Divide', integersOnly: false });
      expect(await calc.getAnswer()).toBe('-6');
    });

    test('TC-035: Phép chia số âm cho số dương (-40 / 8 = -5)', async () => {
      await calc.performCalculation({ number1: '-40', number2: '8', operation: 'Divide', integersOnly: false });
      expect(await calc.getAnswer()).toBe('-5');
    });

    test('TC-036: Phép chia hai số âm (-50 / (-5) = 10)', async () => {
      await calc.performCalculation({ number1: '-50', number2: '-5', operation: 'Divide', integersOnly: false });
      expect(await calc.getAnswer()).toBe('10');
    });

    test('TC-037: Phép chia một số cho 1 (77 / 1 = 77)', async () => {
      await calc.performCalculation({ number1: '77', number2: '1', operation: 'Divide', integersOnly: false });
      expect(await calc.getAnswer()).toBe('77');
    });

    test('TC-038: Phép chia một số cho -1 (64 / (-1) = -64)', async () => {
      await calc.performCalculation({ number1: '64', number2: '-1', operation: 'Divide', integersOnly: false });
      expect(await calc.getAnswer()).toBe('-64');
    });

    test('TC-039: Phép chia 0 cho một số khác 0 (0 / 9 = 0)', async () => {
      await calc.performCalculation({ number1: '0', number2: '9', operation: 'Divide', integersOnly: false });
      expect(await calc.getAnswer()).toBe('0');
    });

    test('TC-040: Phép chia hai số thập phân (7.5 / 2.5 = 3)', async () => {
      await calc.performCalculation({ number1: '7.5', number2: '2.5', operation: 'Divide', integersOnly: false });
      expect(await calc.getAnswer()).toBe('3');
    });
  });

  // =========================================================================
  // TS-005: DIVISION BY ZERO (TC-041 -> TC-042)
  // =========================================================================
  test.describe('TS-005: Division by Zero', () => {
    test('TC-041: Bắt lỗi chia cho số 0 (15 / 0)', async () => {
      await calc.performCalculation({ number1: '15', number2: '0', operation: 'Divide' });
      expect(await calc.getErrorMessage()).toBe('Divide by zero error!');
    });

    test('TC-042: Bắt lỗi chia 0 cho 0 (0 / 0)', async () => {
      await calc.performCalculation({ number1: '0', number2: '0', operation: 'Divide' });
      expect(await calc.getErrorMessage()).toBe('Divide by zero error!');
    });
  });

  // =========================================================================
  // TS-006: CONCATENATE (TC-043 -> TC-052)
  // =========================================================================
  test.describe('TS-006: Concatenate', () => {
    test('TC-043: Nối chuỗi hai số nguyên (12 và 34 -> 1234)', async () => {
      await calc.performCalculation({ number1: '12', number2: '34', operation: 'Concatenate' });
      expect(await calc.getAnswer()).toBe('1234');
    });

    test('TC-044: Nối chuỗi có chữ số 0 đứng đầu (01 và 05 -> 0105)', async () => {
      await calc.performCalculation({ number1: '01', number2: '05', operation: 'Concatenate' });
      expect(await calc.getAnswer()).toBe('0105');
    });

    test('TC-045: Nối chuỗi với số 0 đơn lẻ (50 và 0 -> 500)', async () => {
      await calc.performCalculation({ number1: '50', number2: '0', operation: 'Concatenate' });
      expect(await calc.getAnswer()).toBe('500');
    });

    test('TC-046: Nối chuỗi với số âm (-10 và -20 -> -10-20)', async () => {
      await calc.performCalculation({ number1: '-10', number2: '-20', operation: 'Concatenate' });
      expect(await calc.getAnswer()).toBe('-10-20');
    });

    test('TC-047: Nối chuỗi với số thập phân (3.14 và 2.5 -> 3.142.5)', async () => {
      await calc.performCalculation({ number1: '3.14', number2: '2.5', operation: 'Concatenate' });
      expect(await calc.getAnswer()).toBe('3.142.5');
    });

    test('TC-048: Nối chuỗi văn bản chữ cái (Hello và World -> HelloWorld)', async () => {
      await calc.performCalculation({ number1: 'Hello', number2: 'World', operation: 'Concatenate' });
      expect(await calc.getAnswer()).toBe('HelloWorld');
      expect(await calc.getErrorMessage()).toBe('');
    });

    test('TC-049: Nối chuỗi chữ và số (Test và 123 -> Test123)', async () => {
      await calc.performCalculation({ number1: 'Test', number2: '123', operation: 'Concatenate' });
      expect(await calc.getAnswer()).toBe('Test123');
    });

    test('TC-050: Nối chuỗi ký tự đặc biệt (#@ và &$ -> #@&$)', async () => {
      await calc.performCalculation({ number1: '#@', number2: '&$', operation: 'Concatenate' });
      expect(await calc.getAnswer()).toBe('#@&$');
    });

    test('TC-051: Nối chuỗi khi First number để trống (rỗng và 999 -> 999)', async () => {
      await calc.performCalculation({ number1: '', number2: '999', operation: 'Concatenate' });
      expect(await calc.getAnswer()).toBe('999');
    });

    test('TC-052: Nối chuỗi khi cả hai trường đều để trống (rỗng và rỗng -> rỗng)', async () => {
      await calc.performCalculation({ number1: '', number2: '', operation: 'Concatenate' });
      expect(await calc.getAnswer()).toBe('');
    });
  });

  // =========================================================================
  // TS-007 & TS-008: INTEGERS ONLY & UI DEPENDENCY (TC-053 -> TC-060)
  // =========================================================================
  test.describe('TS-007 & TS-008: Integers only & UI Dependency', () => {
    test('TC-053: Integers only = ON với kết quả là số nguyên chính xác (20 / 5 = 4)', async () => {
      await calc.performCalculation({ number1: '20', number2: '5', operation: 'Divide', integersOnly: true });
      expect(await calc.getAnswer()).toBe('4');
    });

    test('TC-054: Integers only = ON với kết quả số thập phân dương cắt đuôi (10 / 3 = 3)', async () => {
      await calc.performCalculation({ number1: '10', number2: '3', operation: 'Divide', integersOnly: true });
      expect(await calc.getAnswer()).toBe('3');
    });

    test('TC-055: Integers only = ON với số thập phân dương sát số nguyên trên (7.99 + 0 = 7)', async () => {
      await calc.performCalculation({ number1: '7.99', number2: '0', operation: 'Add', integersOnly: true });
      expect(await calc.getAnswer()).toBe('7');
    });

    test('TC-056: Integers only = ON với kết quả số thập phân âm (-7 / 2 = -3)', async () => {
      await calc.performCalculation({ number1: '-7', number2: '2', operation: 'Divide', integersOnly: true });
      expect(await calc.getAnswer()).toBe('-3');
    });

    test('TC-057: Integers only = ON với kết quả trong khoảng (0, 1) (1 / 4 = 0)', async () => {
      await calc.performCalculation({ number1: '1', number2: '4', operation: 'Divide', integersOnly: true });
      expect(await calc.getAnswer()).toBe('0');
    });

    test('TC-058: Bật/tắt Integers only sau khi đã có kết quả tính', async () => {
      await calc.performCalculation({ number1: '11', number2: '4', operation: 'Divide', integersOnly: false });
      expect(await calc.getAnswer()).toBe('2.75');
      // Dynamic toggle
      await calc.setIntegersOnly(true);
      expect(await calc.getAnswer()).toBe('2');
    });

    test('TC-059: Ẩn và vô hiệu hóa Integers only khi chọn Concatenate', async () => {
      await calc.selectOperation('Concatenate');
      await expect(calc.integerSelect).toBeHidden();
      await expect(calc.intSelectionLabel).toBeHidden();
      await expect(calc.integerSelect).toBeDisabled();
    });

    test('TC-060: Hiển thị lại Integers only khi chuyển từ Concatenate sang Add', async () => {
      await calc.selectOperation('Concatenate');
      await expect(calc.integerSelect).toBeHidden();
      await calc.selectOperation('Add');
      await expect(calc.integerSelect).toBeVisible();
      await expect(calc.integerSelect).toBeEnabled();
    });
  });

  // =========================================================================
  // TS-009 & TS-010: INPUT VALIDATION & BOUNDARY (TC-061 -> TC-068)
  // =========================================================================
  test.describe('TS-009 & TS-010: Input Validation & Boundary', () => {
    test('TC-061: Validation lỗi khi First number là chữ cái (abc + 10)', async () => {
      await calc.performCalculation({ number1: 'abc', number2: '10', operation: 'Add' });
      expect(await calc.getErrorMessage()).toBe('Number 1 is not a number');
    });

    test('TC-062: Validation lỗi khi Second number là chữ cái (25 + xyz)', async () => {
      await calc.performCalculation({ number1: '25', number2: 'xyz', operation: 'Add' });
      expect(await calc.getErrorMessage()).toBe('Number 2 is not a number');
    });

    test('TC-063: Ưu tiên báo lỗi Number 1 khi cả hai trường đều là chữ (aaa - bbb)', async () => {
      await calc.performCalculation({ number1: 'aaa', number2: 'bbb', operation: 'Subtract' });
      expect(await calc.getErrorMessage()).toBe('Number 1 is not a number');
    });

    test('TC-064: Validation lỗi với ký tự đặc biệt (@#$% * 5)', async () => {
      await calc.performCalculation({ number1: '@#$%', number2: '5', operation: 'Multiply' });
      expect(await calc.getErrorMessage()).toBe('Number 1 is not a number');
    });

    test('TC-065: Validation lỗi với nhiều dấu chấm thập phân (12.3.4 / 6)', async () => {
      await calc.performCalculation({ number1: '12.3.4', number2: '6', operation: 'Divide' });
      expect(await calc.getErrorMessage()).toBe('Number 1 is not a number');
    });

    test('TC-066: Kiểm tra xử lý trường để trống trong phép tính số học (Empty + 10)', async () => {
      await calc.performCalculation({ number1: '', number2: '10', operation: 'Add' });
      // Ghi nhận actual behavior: Prototype coi '' là 0 và ra 10
      const ans = await calc.getAnswer();
      expect(ans).toBe('10');
    });

    test('TC-067: Kiểm tra xử lý khoảng trắng trong phép tính số học ("   " + 8)', async () => {
      await calc.setFirstNumber('   ');
      await calc.setSecondNumber('8');
      await calc.selectOperation('Add');
      await calc.calculate();
      // Ghi nhận actual behavior: Prototype coi khoảng trắng là 0
      const ans = await calc.getAnswer();
      expect(ans).toBe('8');
    });

    test('TC-068: Giới hạn độ dài nhập liệu tối đa 10 ký tự', async () => {
      await calc.number1Field.pressSequentially('1234567890123');
      const val = await calc.number1Field.inputValue();
      expect(val).toBe('1234567890');
      expect(val.length).toBe(10);
    });
  });

  // =========================================================================
  // TS-011 & TS-012: CLEAR & UI CONTROLS (TC-069, TC-070, TC-080)
  // =========================================================================
  test.describe('TS-011 & TS-012: Clear & UI Controls', () => {
    test('TC-069: Nút Clear xóa kết quả hiển thị và uncheck Integers only', async () => {
      await calc.performCalculation({ number1: '50', number2: '20', operation: 'Add', integersOnly: true });
      expect(await calc.getAnswer()).toBe('70');
      expect(await calc.integerSelect.isChecked()).toBe(true);

      await calc.clear();
      expect(await calc.getAnswer()).toBe('');
      expect(await calc.integerSelect.isChecked()).toBe(false);
      // First number và Second number vẫn giữ nguyên
      expect(await calc.number1Field.inputValue()).toBe('50');
      expect(await calc.number2Field.inputValue()).toBe('20');
    });

    test('TC-070: Nút Clear xóa thông báo lỗi', async () => {
      await calc.performCalculation({ number1: 'abc', number2: '10', operation: 'Add' });
      expect(await calc.getErrorMessage()).toBe('Number 1 is not a number');

      await calc.clear();
      expect(await calc.getErrorMessage()).toBe('');
    });

    test('TC-080: Kiểm tra trạng thái calculating spinner và disable controls', async () => {
      await calc.setFirstNumber('50');
      await calc.setSecondNumber('50');
      await calc.selectOperation('Add');
      await calc.calculateButton.click();
      
      await expect(calc.answerField).toBeVisible();
      expect(await calc.getAnswer()).toBe('100');
    });
  });

  // =========================================================================
  // TS-013: BUILD REGRESSION TESTING (TC-071 -> TC-079)
  // =========================================================================
  test.describe('TS-013: Build Regression Testing', () => {
    test('TC-071: Build 1 - Phát hiện lỗi bỏ qua Input Validation', async () => {
      await calc.selectBuild('1');
      await calc.performCalculation({ build: '1', number1: 'abc', number2: '10', operation: 'Add' });
      expect(await calc.getErrorMessage()).toBe('');
      expect(await calc.getAnswer()).toBe('NaN');
    });

    test('TC-072: Build 2 - Phát hiện lỗi tráo đổi Add và Concatenate', async () => {
      await calc.selectBuild('2');
      await calc.performCalculation({ build: '2', number1: '10', number2: '20', operation: 'Add' });
      expect(await calc.getAnswer()).toBe('1020');
    });

    test('TC-073: Build 3 - Phát hiện lỗi Concatenate bị ép kiểu số học', async () => {
      await calc.selectBuild('3');
      await calc.performCalculation({ build: '3', number1: 'Hello', number2: 'World', operation: 'Concatenate' });
      expect(await calc.getErrorMessage()).toBe('Number 1 is not a number');
    });

    test('TC-074: Build 4 - Phát hiện lỗi tùy chọn Integers only bị khóa cứng', async () => {
      await calc.selectBuild('4');
      await expect(calc.integerSelect).toBeChecked();
      await expect(calc.integerSelect).toBeDisabled();

      await calc.performCalculation({ build: '4', number1: '10', number2: '4', operation: 'Divide' });
      expect(await calc.getAnswer()).toBe('2');
    });

    test('TC-075: Build 5 - Phát hiện lỗi nút Clear bị vô hiệu hóa', async () => {
      await calc.selectBuild('5');
      await expect(calc.clearButton).toBeDisabled();
    });

    test('TC-076: Build 6 - Phát hiện lỗi thiếu kiểm tra chia cho 0', async () => {
      await calc.selectBuild('6');
      await calc.performCalculation({ build: '6', number1: '12', number2: '0', operation: 'Divide' });
      expect(await calc.getErrorMessage()).toBe('');
      expect(await calc.getAnswer()).toBe('Infinity');
    });

    test('TC-077: Build 7 - Phát hiện lỗi dùng Answer cũ làm Number 1', async () => {
      await calc.selectBuild('7');
      await calc.performCalculation({ build: '7', number1: '10', number2: '5', operation: 'Add' });
      await calc.performCalculation({ build: '7', number1: '100', number2: '2', operation: 'Add' });
      expect(await calc.getAnswer()).toBe('7');
    });

    test('TC-078: Build 8 - Phát hiện lỗi đảo ngược vị trí toán hạng (First và Second)', async () => {
      await calc.selectBuild('8');
      await calc.performCalculation({ build: '8', number1: '10', number2: '2', operation: 'Subtract' });
      expect(await calc.getAnswer()).toBe('-8');
    });

    test('TC-079: Build 9 - Phát hiện phần tử giao diện bị ẩn và vô hiệu hóa', async () => {
      await calc.selectBuild('9');
      await expect(calc.number2Field).toBeHidden();
      await expect(calc.number2Field).toBeDisabled();
      await expect(calc.calculateButton).toBeHidden();
      await expect(calc.calculateButton).toBeDisabled();
    });
  });
});
