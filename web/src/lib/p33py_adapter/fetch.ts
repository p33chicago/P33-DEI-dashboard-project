import { assets } from '$app/paths';

type Fetch = (url: string) => ReturnType<typeof fetch>;
const fetch_json = async (fetch: Fetch): Promise<Record<string, any>[]> =>
	await Promise.all([
		(await fetch(`${assets}/equity_indices/lifestages.json`)).json(),
		(await fetch(`${assets}/equity_indices/indicators.json`)).json()
	]);
export { fetch_json };
