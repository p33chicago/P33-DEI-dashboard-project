import type { Indicator } from '$lib/domain/Indicator.ts';
import { from_route } from '$lib/domain/Indicator.ts';
import type { Lifestage } from '$lib/domain/Lifestage.ts';
import { lifestages } from '$lib/domain/Lifestage.ts';
import type { Scorecard } from '$lib/domain/Scorecard.ts';
import type * as P33Py from './types.ts';

// Maps p33py output to our domain models (things in $lib/domain)

const indicator_from_json = (json_indicator: P33Py.Indicator): Indicator => ({
	...from_route[json_indicator.dimension],
	score: json_indicator.EI_dim_weighted
});

const matches_lifestage =
	(lifestage: Lifestage) => (p33_lifestage_or_indicator: P33Py.Lifestage | P33Py.Indicator) => {
		return p33_lifestage_or_indicator.stage === lifestage.route;
	};

const scorecard_from_ei_json = (
	lifestages_json: P33Py.Lifestage[],
	indicators_json: P33Py.Indicator[]
): Scorecard =>
	lifestages.map((lifestage: Lifestage) => ({
		...lifestage,
		area: 'Chicago Public Schools', // TODO update p33py to export "var_scope" for area
		score: lifestages_json.find(matches_lifestage(lifestage))?.weighted_EI_stage,
		indicators: indicators_json.filter(matches_lifestage(lifestage)).map(indicator_from_json)
	}));

export { scorecard_from_ei_json };
