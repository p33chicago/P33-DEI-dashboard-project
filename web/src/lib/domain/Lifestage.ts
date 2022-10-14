import type { GeographicArea } from './GeographicArea';

type LifestageName = 'K-8' | 'High School' | 'College' | 'Career';
type LifestageRoute = 'k8' | 'hs' | 'college' | 'career';

interface Lifestage {
	name: LifestageName;
	route: LifestageRoute;
	area: GeographicArea;
	score?: number;
}

const k8: Lifestage = {
	name: 'K-8',
	route: 'k8',
	area: 'Chicago Public Schools'
};

const highSchool: Lifestage = {
	name: 'High School',
	route: 'hs',
	area: 'Chicago Public Schools'
};

const college: Lifestage = {
	name: 'College',
	route: 'college',
	area: 'Illinois'
};

const career: Lifestage = {
	name: 'Career',
	route: 'career',
	area: 'Chicago MSA'
};

const lifestages: Lifestage[] = [k8, highSchool, college, career];

export type { LifestageName, LifestageRoute, Lifestage };

export { lifestages, k8 as default_lifestage, k8, highSchool, college, career };
