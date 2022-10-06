import {career, college, highSchool, k8} from "./domain/Lifestage";
import type {Indicator} from "$lib/domain/Indicator";
import {access, excellence, proficiency} from "$lib/domain/Indicator";
import type {Scorecard} from "$lib/domain/Scorecard";
import {assets} from "$app/paths";

type JSONStage = 'k8' | 'hs' | 'col' | 'emp';
type JSONRegion = 'city_chi' | 'region_chi_msa' | 'state_il';
type JSONIndicator = 'access' | 'excellence' | 'proficiency';

// Example: {
//     "weighted_EI_stage": 56.6752663607,
//     "stage": "col"
// }
interface LifestageJson {
    stage: JSONStage;
    weighted_EI_stage: number;
}

// Example: {
//     "var_scope": "city_chi",
//     "stage": "hs",
//     "dimension": "access",
//     "EI_dim_weighted": 54.6988746256
// }
interface IndicatorJson {
    var_scope: JSONRegion;
    stage: JSONStage;
    dimension: JSONIndicator;
    EI_dim_weighted: number;
}

type Fetch = (url: string) => ReturnType<typeof fetch>
const fetch_json = async (fetch: Fetch): Promise<[LifestageJson[], IndicatorJson[]]> => await Promise.all([
    (await fetch(`${assets}/equity_indices/lifestages.json`)).json(),
    (await fetch(`${assets}/equity_indices/indicators.json`)).json(),
])

const indicator_from_json = (json_indicator: IndicatorJson): Indicator => ({
    access: {...access, score: json_indicator.EI_dim_weighted},
    proficiency: {...proficiency, score: json_indicator.EI_dim_weighted},
    excellence: {...excellence, score: json_indicator.EI_dim_weighted},
}[json_indicator.dimension])

const from_json = (lifestages: LifestageJson[], indicators: IndicatorJson[]): Scorecard => ([
    {
        ...k8,
        area: 'Chicago Public Schools',
        score: lifestages.find(l => l.stage === 'k8')?.weighted_EI_stage,
        indicators: indicators.filter(i => i.stage === 'k8').map(indicator_from_json)
    },
    {
        ...highSchool,
        area: 'Chicago Public Schools',
        score: lifestages.find(l => l.stage === 'hs')?.weighted_EI_stage,
        indicators: indicators.filter(i => i.stage === 'hs').map(indicator_from_json)
    },
    {
        ...college,
        area: 'Illinois',
        score: lifestages.find(l => l.stage === 'col')?.weighted_EI_stage,
        indicators: indicators.filter(i => i.stage === 'col').map(indicator_from_json)
    },
    {
        ...career,
        area: 'Chicago MSA',
        score: lifestages.find(l => l.stage === 'emp')?.weighted_EI_stage,
        indicators: indicators.filter(i => i.stage === 'emp').map(indicator_from_json)
    }
])
export {fetch_json, from_json};