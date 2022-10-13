<script lang="ts">
	import { page } from '$app/stores';
	import { assets, base } from '$app/paths';
	import { lifestages } from '$lib/domain/Lifestage';
	import Hamburger from './icons/Hamburger.svelte';
	import Cross from './icons/Cross.svelte';
	import LifestageSubnav from './LifestageSubnav.svelte';
	import * as Scorecard from '$lib/domain/Scorecard';

	let nav_checkbox;
	const hide_nav = () => (nav_checkbox.checked = false);
</script>

<input bind:this={nav_checkbox} class="hidden" id="open-mobile-menu" type="checkbox" />
<header
	class="z-10 md:static bg-white font-mono w-full items-center fullnav:border-b border-brand-primary-green z-10"
>
	<div class="align-top justify-left">
		<div class="px-1 md:px-3 lg:px-6 flex justify-between fullnav:justify-start">
			<label
				aria-controls="mobile-menu"
				aria-expanded="false"
				class="toggle-mobile-menu flex fullnav:hidden items-center justify-center p-2"
				for="open-mobile-menu"
			>
				<span class="sr-only">Open main menu</span>
				<Hamburger />
				<Cross />
			</label>
			<div class="logo flex p-2" on:click={hide_nav}>
				<a class="" href={`${base}/`}>
					<img alt="" class="h-8 w-8 sm:mr-10" src={`${assets}/p33-logo.png`} />
				</a>
			</div>

			<div class="flex fullnav:hidden h-10 w-10">
				<!-- placeholder to keep logo centered -->
				<div />
			</div>

			<nav
				class="hidden fullnav:flex z-50 w-full fullnav:w-auto absolute fullnav:static top-12 left-0 right-0 bottom-0 bg-white fullnav:bg-transparent p-4 fullnav:p-0 leading-10 border-t fullnav:border-0 border-brand-primary-green h-screen fullnav:h-auto"
			>
				<ul class="fullnav:flex" on:click={hide_nav}>
					<li class:active={$page.url.pathname === `${base}/${Scorecard.route}`}>
						<a class="h-full w-full" href={`${base}/${Scorecard.route}`}>{Scorecard.name}</a>
					</li>
					{#each lifestages as lifestage}
						<li class="fullnav:hidden pl-4 pt-1 pb-2">
							<LifestageSubnav {lifestage} />
						</li>
					{/each}
					<li class:active={$page.url.pathname === `${base}/solutions`}>
						<a href={`${base}/solutions`}>Solutions</a>
					</li>
					<li class:active={$page.url.pathname === `${base}/about`}>
						<a href={`${base}/about`}>About Us</a>
					</li>
					<li class:active={$page.url.pathname === `${base}/contact`}>
						<a href={`${base}/contact`}>Contact Us</a>
					</li>
				</ul>
			</nav>
		</div>
	</div>
</header>

<style>
	.logo img {
		filter: invert() brightness(85%) sepia(20%) hue-rotate(120deg);
	}

	:checked ~ header {
		position: fixed;
		top: 0;
		bottom: 0;
		left: 0;
		right: 0;
		z-index: 10;
		overflow: scroll;
	}
	@media screen(md) {
		:checked ~ header {
			position: static;
			top: auto;
			bottom: auto;
			left: auto;
			right: auto;
			z-index: auto;
			overflow: auto;
		}
	}

	:checked ~ header :global(.hamburger) {
		display: none;
	}

	:checked ~ header :global(.cross) {
		display: flex;
	}

	:checked ~ header nav {
		display: block;
	}

	nav li {
		padding: 0.25rem 1rem;
	}

	@media screen(lg) {
		.active {
			border-bottom: 2px solid theme('colors.brand-primary-dark-green');
			font-weight: theme('fontWeight.bold');
		}
	}
</style>
