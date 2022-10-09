import { expect, test } from '@playwright/test';

const float_regex = /[\d.]+/;
const n_floats = (n: number) => [...Array(n)].map(() => float_regex);

test('equity indices', async ({ page }) => {
	await page.goto('/');

	// Lifestages
	await Promise.all([
		// Geographic areas
		// expect(page.locator('data-test-id=scorecard.lifestage-area-k8')).toHaveText(),
		// expect(page.locator('data-test-id=scorecard.lifestage-area-hs')).toHaveText(),
		// expect(page.locator('data-test-id=scorecard.lifestage-area-college')).toHaveText(),
		// expect(page.locator('data-test-id=scorecard.lifestage-area-career')).toHaveText(),

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
test('lifestage figures', async ({ page }) => {
	await page.goto('/');
	await Promise.all([
		expect(page.locator('[data-test-id="scorecard.figure-k8"] svg:first-child')).toBeVisible(),
		expect(page.locator('[data-test-id="scorecard.figure-hs"] svg:first-child')).toBeVisible(),
		expect(page.locator('[data-test-id="scorecard.figure-college"] svg:first-child')).toBeVisible(),
		expect(page.locator('[data-test-id="scorecard.figure-career"] svg:first-child')).toBeVisible()
	]);
});
