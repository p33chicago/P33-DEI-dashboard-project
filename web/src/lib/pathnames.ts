import type { Indicator } from '$lib/domain/Indicator';
import { default_indicator, indicators } from '$lib/domain/Indicator';
import type { Lifestage } from '$lib/domain/Lifestage';
import { default_lifestage, lifestages } from '$lib/domain/Lifestage';

interface Data {
	lifestage?: Lifestage;
	indicator?: Indicator;
}

const default_scorecard_path = `${default_lifestage.route}/${default_indicator.route}`;

const lifestage_pattern = lifestages.map(({ route }: Lifestage) => route).join('|');
const indicator_pattern = indicators.map(({ route }: Indicator) => route).join('|');
const pathname_pattern = new RegExp(`(${lifestage_pattern})(/(${indicator_pattern}))?`);

const data_from_pathname = (pathname: string): Data => {
	const matches = pathname_pattern.exec(pathname);
	if (matches === null) {
		return { lifestage: null, indicator: null };
	}
	const lifestage_path = matches[1];
	const indicator_path = matches[3];
	const lifestage = lifestages.find(({ route }: Lifestage) => route === lifestage_path);
	const indicator = indicators.find(({ route }: Indicator) => route === indicator_path);
	return { lifestage, indicator };
};

export type { Data };

export { default_scorecard_path, pathname_pattern, data_from_pathname };
