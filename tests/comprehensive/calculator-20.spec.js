import { test, expect } from '@playwright/test';
import { CalculatorPage } from './pages/CalculatorPage.js';

test.describe('Basic Calculator Automation Suite - 20 Extra Test Cases (TC-081 to TC-100)', () => {
  /** @type {CalculatorPage} */
  let calc;

  test.beforeEach(async ({ page }) => {
    calc = new CalculatorPage(page);
    await calc.goto();
    // Luôn chạy trên Prototype (Build 0) để có kết quả chuẩn
    await calc.selectBuild('0');
  });

  test('TC-081: Phép chia cho số 0 với số dương (10 / 0)', async () => {
    await calc.performCalculation({ number1: '10', number2: '0', operation: 'Divide' });
    expect(await calc.getErrorMessage()).toBe('Divide by zero error!');
  });

  test('TC-082: Phép chia cho số 0 với số âm (-5 / 0)', async () => {
    await calc.performCalculation({ number1: '-5', number2: '0', operation: 'Divide' });
    expect(await calc.getErrorMessage()).toBe('Divide by zero error!');
  });

  test('TC-083: Phép chia số 0 cho số 0 (0 / 0)', async () => {
    await calc.performCalculation({ number1: '0', number2: '0', operation: 'Divide' });
    expect(await calc.getErrorMessage()).toBe('Divide by zero error!');
  });

  test('TC-084: Ghép 2 chuỗi số nguyên (12 + 34 = 1234)', async () => {
    await calc.performCalculation({ number1: '12', number2: '34', operation: 'Concatenate' });
    expect(await calc.getAnswer()).toBe('1234');
  });

  test('TC-085: Ghép chuỗi chữ và số (abc + 123 = abc123)', async () => {
    await calc.performCalculation({ number1: 'abc', number2: '123', operation: 'Concatenate' });
    expect(await calc.getAnswer()).toBe('abc123');
  });

  test('TC-086: Ghép chuỗi chứa khoảng trắng (Hello + World = Hello World)', async () => {
    await calc.performCalculation({ number1: 'Hello ', number2: 'World', operation: 'Concatenate' });
    expect(await calc.getAnswer()).toBe('Hello World');
  });

  test('TC-087: Validation lỗi nhập Number 1 không phải là số', async () => {
    await calc.performCalculation({ number1: 'xyz', number2: '10', operation: 'Add' });
    expect(await calc.getErrorMessage()).toBe('Number 1 is not a number');
  });

  test('TC-088: Validation lỗi nhập Number 2 không phải là số', async () => {
    await calc.performCalculation({ number1: '10', number2: 'xyz', operation: 'Add' });
    expect(await calc.getErrorMessage()).toBe('Number 2 is not a number');
  });

  test('TC-089: Validation lỗi nhập cả 2 đều không phải số', async () => {
    await calc.performCalculation({ number1: 'abc', number2: 'xyz', operation: 'Add' });
    expect(await calc.getErrorMessage()).toBe('Number 1 is not a number'); // Ưu tiên báo lỗi ô 1 trước
  });

  test('TC-090: Thử tính toán Add với dữ liệu trống', async () => {
    await calc.performCalculation({ number1: '', number2: '', operation: 'Add' });
    expect(await calc.getAnswer()).toBe('0'); 
  });

  test('TC-091: Thử tính toán Concatenate với dữ liệu trống', async () => {
    await calc.performCalculation({ number1: '', number2: '', operation: 'Concatenate' });
    expect(await calc.getAnswer()).toBe('');
  });

  test('TC-092: Phép nhân với số siêu lớn', async () => {
    await calc.performCalculation({ number1: '99999', number2: '99999', operation: 'Multiply' });
    expect(await calc.getAnswer()).toBe('9999800001');
  });

  test('TC-093: Phép chia với kết quả tuần hoàn (10 / 3)', async () => {
    await calc.performCalculation({ number1: '10', number2: '3', operation: 'Divide' });
    expect(await calc.getAnswer()).toBe('3.3333333333333335');
  });

  test('TC-094: Phép chia kết quả tuần hoàn nhưng chọn Integers Only', async () => {
    await calc.performCalculation({ number1: '10', number2: '3', operation: 'Divide', integersOnly: true });
    expect(await calc.getAnswer()).toBe('3');
  });

  test('TC-095: Liên tục thay đổi phép tính mà không cần nhập lại', async () => {
    await calc.setFirstNumber('10');
    await calc.setSecondNumber('5');
    await calc.selectOperation('Add');
    await calc.calculate();
    expect(await calc.getAnswer()).toBe('15');
    
    await calc.selectOperation('Multiply');
    await calc.calculate();
    expect(await calc.getAnswer()).toBe('50');
  });

  test('TC-096: Xóa dữ liệu và kiểm tra validation', async () => {
    await calc.performCalculation({ number1: '5', number2: '5', operation: 'Add' });
    await calc.clear();
    expect(await calc.getAnswer()).toBe('');
    await calc.calculate();
    expect(await calc.getAnswer()).toBe('0');
  });

  test('TC-097: Nhập chuỗi HTML script vào ô số xem có bị lỗi (XSS check)', async () => {
    await calc.performCalculation({ number1: '<script>alert(1)</script>', number2: '2', operation: 'Add' });
    expect(await calc.getErrorMessage()).toBe('Number 1 is not a number');
  });

  test('TC-098: Nhập số khoa học dạng E (1e3 + 2)', async () => {
    await calc.performCalculation({ number1: '1e3', number2: '2', operation: 'Add' });
    expect(await calc.getAnswer()).toBe('1002');
  });

  test('TC-099: Kiểm tra checkbox Integers Only bị Disable với Concatenate', async () => {
    await calc.selectOperation('Concatenate');
    expect(await calc.integerSelect.isDisabled()).toBeTruthy();
  });

  test('TC-100: Kiểm tra checkbox Integers Only Enable với Add', async () => {
    await calc.selectOperation('Add');
    expect(await calc.integerSelect.isEnabled()).toBeTruthy();
  });
});
