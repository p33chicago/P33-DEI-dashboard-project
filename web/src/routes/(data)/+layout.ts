import type { Load } from '@sveltejs/kit';
import { data_from_pathname } from '$lib/pathnames';

export const load: Load = ({ url }) => data_from_pathname(url.pathname);
