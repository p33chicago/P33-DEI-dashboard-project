type LifestageName = 'K-8' | 'High School' | 'College' | 'Career';
type LifestageRoute = 'k8' | 'hs' | 'college' | 'career';

interface Lifestage {
    name: LifestageName;
    route: LifestageRoute;
    score?: number;
}

const k8: Lifestage = {
    name: 'K-8',
    route: 'k8',
}

const highSchool: Lifestage = {
    name: 'High School',
    route: 'hs'
}

const college: Lifestage = {
    name: 'College',
    route: 'college'
}

const career: Lifestage = {
    name: 'Career',
    route: 'career'
}

const lifestages: Lifestage[] = [k8, highSchool, college, career];

export type {
    LifestageName,
    LifestageRoute,
    Lifestage,
}

export {
    lifestages,
    k8,
    highSchool,
    college,
    career
}