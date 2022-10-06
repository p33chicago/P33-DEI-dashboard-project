import type { Lifestage } from './Lifestage';
import type { GeographicArea } from './GeographicArea';
import type { Indicator } from './Indicator';
import { from_json } from '$lib/equity_indices_json';

interface LifestageScore extends Lifestage {
	area: GeographicArea;
	score: number | undefined;
	indicators: Indicator | { score?: number }[];
}

type Scorecard = LifestageScore[];

export type { Scorecard, LifestageScore };

export { from_json };
