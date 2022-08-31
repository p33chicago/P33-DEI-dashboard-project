import { browser } from '$app/env';

let Plotly: typeof import('plotly.js');

export const load = async (): Promise<boolean | Plotly> => {
    if (!browser) {
        return false;
    }
    if (Plotly) {
        return Plotly;
    }
    console.log('Loading');
    Plotly = await import('plotly.js/dist/plotly-basic.min.js');
    return Plotly;
};