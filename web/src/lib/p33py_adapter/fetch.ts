import { assets } from '$app/paths';
import type { Indicator, Lifestage } from './types.ts';

type Fetch = (url: string) => ReturnType<typeof fetch>;
const fetch_json = async (fetch: Fetch): Promise<[Lifestage[], Indicator[]]> =>
	await Promise.all([
		(await fetch(`${assets}/scorecard/lifestages.json`)).json(),
		(await fetch(`${assets}/scorecard/indicators.json`)).json()
	]);
export { fetch_json };
