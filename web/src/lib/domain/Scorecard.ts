import type {Lifestage} from "./Lifestage";
import type {GeographicArea} from "./GeographicArea";
import type {Indicator} from "./Indicator";

interface LifestageScore extends Lifestage {
    area: GeographicArea;
    score: number;
    indicators: Indicator[];
}

type Scorecard = LifestageScore[];

const scorecard: Scorecard = [
    {
        name: 'K-8',
        area: 'Chicago Public Schools',
        route: 'k8',
        score: 46.6,
        indicators: [
            {name: 'Access', route: 'access', score: 67.1},
            {name: 'Proficiency', route: 'proficiency', score: 73.4},
            {name: 'Excellence', route: 'excellence', score: 77.2},
        ]
    },
    {
        name: 'High School',
        area: 'Chicago Public Schools',
        route: 'hs',
        score: 53.1,
        indicators: [
            {name: 'Access', route: 'access', score: 67.1},
            {name: 'Proficiency', route: 'proficiency', score: 73.4},
            {name: 'Excellence', route: 'excellence', score: 77.2},
        ]
    },
    {
        name: 'College',
        area: 'Illinois',
        route: 'college',
        score: 74.2,
        indicators: [
            {name: 'Access', route: 'access', score: 67.1},
            {name: 'Proficiency', route: 'proficiency', score: 73.4},
            {name: 'Excellence', route: 'excellence', score: 77.2},
        ]
    },
    {
        name: 'Career',
        area: 'Chicago MSA',
        route: 'career',
        score: 63.2,
        indicators: [
            {name: 'Access', route: 'access', score: 67.1},
            {name: 'Proficiency', route: 'proficiency', score: 73.4},
            {name: 'Excellence', route: 'excellence', score: 77.2},
        ]
    }
]

export type {
    Scorecard,
    LifestageScore
}

export {
    scorecard
}