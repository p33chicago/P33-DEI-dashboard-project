import type { Lifestage } from '../domain/Lifestage';
import type { LifestageName as P33PyLifestageName } from './types';

const p33py_to_domain: Record<P33PyLifestageName, Lifestage['route']> = {
	k8: 'k8',
	hs: 'hs',
	col: 'college',
	emp: 'career'
};

const domain_to_p33py: Record<Lifestage['route'], P33PyLifestageName> = {
	k8: 'k8',
	hs: 'hs',
	college: 'col',
	career: 'emp'
};

export { p33py_to_domain, domain_to_p33py };
