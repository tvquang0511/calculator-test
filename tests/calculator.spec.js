import { test, expect } from '@playwright/test';
import { CalculatorPage } from './comprehensive/pages/CalculatorPage.js';

test.describe('Basic Calculator - Prototype Baseline Suite', () => {
  let calc;

  test.beforeEach(async ({ page }) => {
    calc = new CalculatorPage(page);
    await calc.goto();
    await calc.selectBuild('0'); // Prototype
  });

  test('TC-UI-001: Kiểm tra tính khả dụng và hiển thị của các thành phần giao diện', async () => {
    await expect(calc.number1Field).toBeVisible();
    await expect(calc.number2Field).toBeVisible();
    await expect(calc.calculateButton).toBeVisible();
    await expect(calc.clearButton).toBeEnabled();
  });

  test('TC-UI-002: Kiểm tra chức năng và trạng thái của Checkbox "Integers only"', async () => {
    await calc.performCalculation({ number1: '5.8', number2: '1', operation: 'Divide', integersOnly: true });
    expect(await calc.getAnswer()).toBe('5');

    await calc.setIntegersOnly(false);
    expect(await calc.getAnswer()).toBe('5.8');
  });

  test('TC-UI-003: Kiểm tra chức năng nút "Clear" để reset giao diện', async () => {
    await calc.performCalculation({ number1: '10', number2: '20', operation: 'Add' });
    await calc.clear();
    expect(await calc.getAnswer()).toBe('');
  });

  test('TC-MATH-001: Kiểm tra tính đúng đắn của phép tính cộng', async () => {
    await calc.performCalculation({ number1: '10', number2: '20', operation: 'Add' });
    expect(await calc.getAnswer()).toBe('30');
  });

  test('TC-MATH-002: Kiểm tra phép tính trừ và thứ tự toán tử', async () => {
    await calc.performCalculation({ number1: '15', number2: '5', operation: 'Subtract' });
    expect(await calc.getAnswer()).toBe('10');
  });

  test('TC-MATH-003: Kiểm tra phép tính chia ra kết quả số thập phân', async () => {
    await calc.performCalculation({ number1: '7', number2: '2', operation: 'Divide' });
    expect(await calc.getAnswer()).toBe('3.5');
  });

  test('TC-MATH-004: Kiểm tra xử lý ngoại lệ phép chia cho 0', async () => {
    await calc.performCalculation({ number1: '10', number2: '0', operation: 'Divide' });
    expect(await calc.getErrorMessage()).toBe('Divide by zero error!');
  });

  test('TC-MATH-005: Kiểm tra tính độc lập giữa các lần tính toán liên tiếp', async () => {
    await calc.performCalculation({ number1: '2', number2: '3', operation: 'Add' });
    expect(await calc.getAnswer()).toBe('5');

    await calc.setFirstNumber('10');
    await calc.setSecondNumber('20');
    await calc.calculate();
    expect(await calc.getAnswer()).toBe('30');
  });

  test('TC-STR-001: Kiểm tra chức năng ghép chuỗi văn bản', async () => {
    await calc.performCalculation({ number1: 'Hello', number2: 'World', operation: 'Concatenate' });
    expect(await calc.getAnswer()).toBe('HelloWorld');
  });

  test('TC-VAL-001: Bắt lỗi khi nhập ký tự không phải số trong phép toán số học', async () => {
    await calc.performCalculation({ number1: 'abc', number2: '10', operation: 'Add' });
    expect(await calc.getErrorMessage()).toBe('Number 1 is not a number');
  });
});
