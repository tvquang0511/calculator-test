import { defineConfig, devices } from '@playwright/test';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const localHtml = path.resolve(__dirname, 'src/basicCalculator.html').replace(/\\/g, '/');
const localHtmlUrl = localHtml.startsWith('/') ? `file://${localHtml}` : `file:///${localHtml}`;

export default defineConfig({
  testDir: './tests',
  testMatch: '**/*.spec.js',
  timeout: 30000,
  fullyParallel: false,
  reporter: [
    ['list'],
    ['html', { outputFolder: 'playwright-report', open: 'never' }]
  ],
  use: {
    baseURL: localHtmlUrl,
    headless: true,
    screenshot: 'only-on-failure',
    video: 'retain-on-failure',
  },
  projects: [
    {
      name: 'chromium',
      use: { 
        ...devices['Desktop Chrome'],
        // Trên máy local Windows dùng Google Chrome nếu có, trên CI dùng Playwright Chromium mặc định
        ...(process.env.CI ? {} : { channel: 'chrome' })
      },
    },
  ],
});
