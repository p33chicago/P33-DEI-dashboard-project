// import { test as base } from '@playwright/test';
// import { readFile } from 'fs/promises';
// import { scorecard_from_ei_json } from './p33py_adapter.js';

// fixtures
// const test = base.extend<{
// 	json: {
// 		lifestages: Record<string, any>;
// 		indicators: Record<string, any>;
// 	};
// }>({
// 	json: async ({}, use) => {
// 		await use({
// 			lifestages: JSON.parse(await readFile(`static/equity_indices/lifestages.json`, 'utf-8')),
// 			indicators: JSON.parse(await readFile(`static/equity_indices/indicators.json`, 'utf-8'))
// 		});
// 	}
// });

import { expect, test } from '@playwright/test';

const float_regex = /[\d.]+/;
const n_floats = (n: number) => [...Array(n)].map((i) => float_regex);

test.fixme('equity indices', async ({ page }) => {
	await page.goto('/');

	// Lifestages
	await Promise.all([
		// Geographic areas
		expect(page.locator('data-test-id=scorecard.lifestage-area-k8')).toHaveText(float_regex),
		expect(page.locator('data-test-id=scorecard.lifestage-area-hs')).toHaveText(float_regex),
		expect(page.locator('data-test-id=scorecard.lifestage-area-college')).toHaveText(float_regex),
		expect(page.locator('data-test-id=scorecard.lifestage-area-career')).toHaveText(float_regex),

		// Lifestage scores
		expect(page.locator('data-test-id=scorecard.lifestage-score-k8')).toHaveText(float_regex),
		expect(page.locator('data-test-id=scorecard.lifestage-score-hs')).toHaveText(float_regex),
		expect(page.locator('data-test-id=scorecard.lifestage-score-college')).toHaveText(float_regex),
		expect(page.locator('data-test-id=scorecard.lifestage-score-career')).toHaveText(float_regex)
	]);

	// Indicators
	// Access
	const access = page.locator('data-test-id=scorecard.indicator-score-access');
	await expect(access).toContainText(n_floats(3));

	// Proficiency
	const proficiency = page.locator('data-test-id=scorecard.indicator-score-proficiency');
	await expect(proficiency).toContainText(n_floats(4));

	// Excellence
	const excellence = page.locator('data-test-id=scorecard.indicator-score-excellence');
	await expect(excellence).toContainText(n_floats(4));
});
test('lifestage figures', async () => {});
