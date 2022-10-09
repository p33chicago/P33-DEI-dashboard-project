type LifestageName = 'k8' | 'hs' | 'col' | 'emp';
type Region = 'city_chi' | 'region_chi_msa' | 'state_il';
type IndicatorName = 'access' | 'excellence' | 'proficiency';

// Example: {
//     "weighted_EI_stage": 56.6752663607,
//     "stage": "col"
// }
interface Lifestage {
	stage: LifestageName;
	weighted_EI_stage: number;
}

// Example: {
//     "var_scope": "city_chi",
//     "stage": "hs",
//     "dimension": "access",
//     "EI_dim_weighted": 54.6988746256
// }
interface Indicator {
	var_scope: Region;
	stage: LifestageName;
	dimension: IndicatorName;
	EI_dim_weighted: number;
}

export type { LifestageName, Lifestage, Indicator };
