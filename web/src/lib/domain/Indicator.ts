type IndicatorName = 'Access' | 'Proficiency' | 'Excellence';
type IndicatorRoute = 'access' | 'proficiency' | 'excellence';

interface Indicator {
    name: IndicatorName;
    route: IndicatorRoute;
    score?: number;
}

const access: Indicator = {
    name: 'Access',
    route: 'access'
}

const proficiency: Indicator = {
    name: 'Proficiency',
    route: 'proficiency'
}

const excellence: Indicator = {
    name: 'Excellence',
    route: 'excellence'
}

const indicators = [
    access,
    proficiency,
    excellence
]

export type {
    Indicator
}

export {
    indicators,
    access as default_indicator,
    access,
    proficiency,
    excellence
}