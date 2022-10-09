import type { Lifestage } from './Lifestage';
import type { GeographicArea } from './GeographicArea';
import type { Indicator } from './Indicator';
import { scorecard_from_ei_json } from '../p33py_adapter/p33py_adapter';

interface ScorecardIndicator extends Indicator {
	score?: number;
}

interface LifestageScore extends Lifestage {
	area: GeographicArea;
	score: number | undefined;
	indicators: ScorecardIndicator[];
}

type Scorecard = LifestageScore[];

export type { Scorecard, LifestageScore };

export { scorecard_from_ei_json };
