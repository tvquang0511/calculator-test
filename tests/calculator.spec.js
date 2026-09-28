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

  test('TC01 - UI Elements Availability', async ({ page }) => {
    await expect(page.locator('#number1Field')).toBeVisible();
    await expect(page.locator('#number2Field')).toBeVisible();
    await expect(page.locator('#calculateButton')).toBeVisible();
    await expect(page.locator('#clearButton')).toBeEnabled();
  });

  test('TC02 - Addition Operation (10 + 20 = 30)', async ({ page }) => {
    await page.fill('#number1Field', '10');
    await page.fill('#number2Field', '20');
    await page.selectOption('#selectOperationDropdown', '0');
    await page.click('#calculateButton');
    await waitForCalc(page);
    await expect(page.locator('#numberAnswerField')).toHaveValue('30');
  });

  test('TC03 - Subtraction Operation (15 - 5 = 10)', async ({ page }) => {
    await page.fill('#number1Field', '15');
    await page.fill('#number2Field', '5');
    await page.selectOption('#selectOperationDropdown', '1');
    await page.click('#calculateButton');
    await waitForCalc(page);
    await expect(page.locator('#numberAnswerField')).toHaveValue('10');
  });

  test('TC04 - Division with Decimal (7 / 2 = 3.5)', async ({ page }) => {
    await page.fill('#number1Field', '7');
    await page.fill('#number2Field', '2');
    await page.selectOption('#selectOperationDropdown', '3');
    await page.click('#calculateButton');
    await waitForCalc(page);
    await expect(page.locator('#numberAnswerField')).toHaveValue('3.5');
  });

  test('TC05 - Division by Zero Error Handling', async ({ page }) => {
    await page.fill('#number1Field', '10');
    await page.fill('#number2Field', '0');
    await page.selectOption('#selectOperationDropdown', '3');
    await page.click('#calculateButton');
    await waitForCalc(page);
    await expect(page.locator('#errorMsgField')).toHaveText('Divide by zero error!');
  });

  test('TC06 - Concatenate Strings (Hello + World)', async ({ page }) => {
    await page.selectOption('#selectOperationDropdown', '4');
    await page.fill('#number1Field', 'Hello');
    await page.fill('#number2Field', 'World');
    await page.click('#calculateButton');
    await waitForCalc(page);
    await expect(page.locator('#numberAnswerField')).toHaveValue('HelloWorld');
  });

  test('TC07 - Input Validation for Non-numeric Input', async ({ page }) => {
    await page.fill('#number1Field', 'abc');
    await page.fill('#number2Field', '10');
    await page.selectOption('#selectOperationDropdown', '0');
    await page.click('#calculateButton');
    await waitForCalc(page);
    await expect(page.locator('#errorMsgField')).toHaveText('Number 1 is not a number');
  });

  test('TC08 - Integers Only Checkbox Toggle', async ({ page }) => {
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

  test('TC09 - Clear Button Functionality', async ({ page }) => {
    await page.fill('#number1Field', '10');
    await page.fill('#number2Field', '20');
    await page.selectOption('#selectOperationDropdown', '0');
    await page.click('#calculateButton');
    await waitForCalc(page);
    await page.click('#clearButton');
    await expect(page.locator('#numberAnswerField')).toHaveValue('');
  });

  test('TC10 - Consecutive Calculations Independence', async ({ page }) => {
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
});
