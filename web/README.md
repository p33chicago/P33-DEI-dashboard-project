# Tech Equity Index website

This project uses [SvelteKit](https://kit.svelte.dev/) and [tailwindcss](https://tailwindcss.com/).

## Pre-requisites

Gitpod comes pre-installed with everything you need. If you're developing locally, see [Local development environment](../README.md#Local development environment).

## Developing

Start the dev server:

```bash
npm run dev

# or start the server and open the app in a new browser tab
npm run dev -- --open
```

## Building

To create a production version of your app:

```bash
npm run build
```

You can preview the production build with `npm run preview`.

> To deploy your app, you may need to install an [adapter](https://kit.svelte.dev/docs/adapters) for your target environment.

## Updating math equations

We use [KaTex](https://katex.org) to render math equations on the website using the <MathEquation /> component. See katex.org for [a list of available math symbols](https://katex.org/docs/supported.html).
