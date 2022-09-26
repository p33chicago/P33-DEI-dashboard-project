import adapter from '@sveltejs/adapter-static';
import preprocess from 'svelte-preprocess';

const {ENVIRONMENT} = process.env;
const dev = ENVIRONMENT === 'dev';

/** @type {import('@sveltejs/kit').Config} */
const config = {
    // Consult https://github.com/sveltejs/svelte-preprocess
    // for more information about preprocessors
    preprocess: [
        preprocess({
            postcss: true
        }),
    ],
    kit: {
        paths: {
            base: dev ? '' : '/P33-DEI-dashboard-project'
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
