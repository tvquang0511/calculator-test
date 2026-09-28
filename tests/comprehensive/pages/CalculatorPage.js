import { expect } from '@playwright/test';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const localPath = path.resolve(__dirname, '../../../src/basicCalculator.html').replace(/\\/g, '/');
const defaultLocalHtml = localPath.startsWith('/') ? `file://${localPath}` : `file:///${localPath}`;
const onlineUrl = 'https://testsheepnz.github.io/BasicCalculator.html';

/**
 * Page Object Model for Basic Calculator Page
 * Supports both online URL and local src/basicCalculator.html
 */
export class CalculatorPage {
  /**
   * @param {import('@playwright/test').Page} page
   */
  constructor(page) {
    this.page = page;

    // Locators
    this.buildSelect = page.locator('#selectBuild');
    this.number1Field = page.locator('#number1Field');
    this.number2Field = page.locator('#number2Field');
    this.operationDropdown = page.locator('#selectOperationDropdown');
    this.calculateButton = page.locator('#calculateButton');
    this.clearButton = page.locator('#clearButton');
    this.answerField = page.locator('#numberAnswerField');
    this.integerSelect = page.locator('#integerSelect');
    this.intSelectionLabel = page.locator('#intSelectionLabel');
    this.errorMsgField = page.locator('#errorMsgField');
    this.calculatingForm = page.locator('#calculatingForm');
  }

  /**
   * Navigate to the Basic Calculator page
   * @param {string} [targetUrl]
   */
  async goto(targetUrl) {
    const url = targetUrl || defaultLocalHtml;
    try {
      await this.page.goto(url, { waitUntil: 'domcontentloaded', timeout: 5000 });
    } catch (e) {
      await this.page.goto(onlineUrl, { waitUntil: 'domcontentloaded' });
    }
    await expect(this.calculateButton).toBeVisible();
  }

  /**
   * Select a build version
   * @param {string|number} buildVal - "0" (Prototype), "1", "2", ... "9"
   */
  async selectBuild(buildVal) {
    await this.buildSelect.selectOption(String(buildVal));
  }

  /**
   * Enter First Number
   * @param {string} val
   */
  async setFirstNumber(val) {
    await this.number1Field.fill(String(val));
  }

  /**
   * Enter Second Number
   * @param {string} val
   */
  async setSecondNumber(val) {
    await this.number2Field.fill(String(val));
  }

  /**
   * Select Operation
   * @param {"Add"|"Subtract"|"Multiply"|"Divide"|"Concatenate"|string} op
   */
  async selectOperation(op) {
    /** @type {Record<string, string>} */
    const map = {
      'Add': '0',
      'Subtract': '1',
      'Multiply': '2',
      'Divide': '3',
      'Concatenate': '4'
    };
    const val = map[op] !== undefined ? map[op] : op;
    await this.operationDropdown.selectOption(val);
  }

  /**
   * Set Integers Only checkbox state
   * @param {boolean} checked
   */
  async setIntegersOnly(checked) {
    const isChecked = await this.integerSelect.isChecked();
    if (isChecked !== checked) {
      await this.integerSelect.setChecked(checked);
    }
  }

  /**
   * Click Calculate and wait for result
   */
  async calculate() {
    await this.calculateButton.click();
    // Wait for calculating spinner to finish if visible
    try {
      await this.calculatingForm.waitFor({ state: 'hidden', timeout: 3000 });
    } catch (e) {
      // In case of error (e.g., divide by zero bug where unlockCalculate is not called)
    }
  }

  /**
   * Click Clear button
   */
  async clear() {
    await this.clearButton.click();
  }

  /**
   * Get text of Answer field
   * @returns {Promise<string>}
   */
  async getAnswer() {
    return await this.answerField.inputValue();
  }

  /**
   * Get text of Error message label
   * @returns {Promise<string>}
   */
  async getErrorMessage() {
    return (await this.errorMsgField.innerText()).trim();
  }

  /**
   * Helper to perform a full calculation flow
   */
  async performCalculation({
    build = '0',
    number1 = '',
    number2 = '',
    operation = 'Add',
    integersOnly = false
  }) {
    if (build !== '0') {
      await this.selectBuild(build);
    }
    if (number1 !== '') {
      await this.setFirstNumber(number1);
    }
    if (number2 !== '') {
      await this.setSecondNumber(number2);
    }
    await this.selectOperation(operation);
    
    // Only set integersOnly if it's visible & enabled (not Concatenate)
    if (operation !== 'Concatenate' && await this.integerSelect.isVisible()) {
      await this.setIntegersOnly(integersOnly);
    }

    await this.calculate();
  }
}
