import type { PageLoad } from './$types';
import * as Scorecard from '$lib/domain/Scorecard';
import { fetch_json } from '../lib/p33py_adapter/fetch';

export const load: PageLoad = async ({ fetch }) => {
	const [lifestages, indicators] = await fetch_json(fetch);
	const scorecard = Scorecard.from_json(lifestages, indicators);
	return { scorecard };
};
