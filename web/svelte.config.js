import adapter from '@sveltejs/adapter-static';
import preprocess from 'svelte-preprocess';

const { BASE_PATH = '' } = process.env;

console.log(`BASE_PATH: ${BASE_PATH} (${typeof BASE_PATH})`);

/** @type {import('@sveltejs/kit').Config} */
const config = {
	// Consult https://github.com/sveltejs/svelte-preprocess
	// for more information about preprocessors
	preprocess: [
		preprocess({
			postcss: true
		})
	],
	kit: {
		paths: {
			base: BASE_PATH
		},
		adapter: adapter()
	},
	vitePlugin: {
		experimental: {
			inspector: true
		}
	}
};

export default config;
