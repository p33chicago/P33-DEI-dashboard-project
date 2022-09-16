import type {Load} from "@sveltejs/kit";
import type {Indicator} from '$lib/domain/Indicator.ts';
import {indicators} from '$lib/domain/Indicator.ts';
import type {Lifestage} from "$lib/domain/Lifestage.ts";
import {lifestages} from "$lib/domain/Lifestage.ts";

interface Data {
    lifestage: Lifestage;
    indicator?: Indicator;
}

const lifestage_pattern = lifestages.map(({ route }: Lifestage) => route).join('|');
const indicator_pattern = indicators.map(({ route }: Indicator) => route).join('|');
const pathname_pattern = new RegExp(`(${lifestage_pattern})(/(${indicator_pattern}))?`)

const data_from_pathname = (pathname: string): Data => {
    const matches = pathname_pattern.exec(pathname);
    if (matches === null) {
        throw Error('No lifestage found');
    }
    const lifestage_path = matches[1];
    const indicator_path = matches[3];
    const lifestage = lifestages.find(({route}: Lifestage) => route === lifestage_path)
    const indicator = indicators.find(({route}: Indicator) => route === indicator_path)
    return {lifestage, indicator}
}

export const load: Load = ({ url }) => data_from_pathname(url.pathname);