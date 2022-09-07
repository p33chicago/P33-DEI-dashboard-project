<script lang="ts">
	import { page } from '$app/stores';
	// import Nav from './Nav.svelte'
	let innerWidth: number;
	const tw_fullnav = 810;
</script>

<svelte:window bind:innerWidth />

<header class="w-full items-center fullnav:border-b border-brand-primary-green z-10">
	<div class="flex justify-between fullnav:justify-start mx-auto max-w-7xl">
		<input type="checkbox" id="open-mobile-menu" class="hidden" />
		<label for="open-mobile-menu" class="flex fullnav:hidden toggle-mobile-menu items-center justify-center p-2" aria-controls="mobile-menu" aria-expanded="false">
			<span class="sr-only">Open main menu</span>
			<svg class="hamburger block h-6 w-6" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true">
				<path stroke-linecap="round" stroke-linejoin="round" d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5" />
			</svg>
			<svg class="cross hidden h-6 w-6" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true">
				<path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
			</svg>
		</label>
		<div class="logo flex p-2">
			<a href="/" class="">
				<img src="/p33-logo.png" class="h-8 w-8" />
			</a>
		</div>
		
		<div class="flex fullnav:hidden h-10 w-10"><div> </div></div>

		<nav class="hidden fullnav:flex w-full fullnav:w-auto absolute fullnav:static top-12 left-0 right-0 bottom-0 bg-brand-primary-really-light-green p-4 fullnav:p-0 leading-10 border-t fullnav:border-0 border-brand-primary-green">
			<ul class="fullnav:flex">
				<li class:active={innerWidth > tw_fullnav && $page.url.pathname === "/"}><a href="/">The Data</a></li>
				<li class:active={innerWidth > tw_fullnav && $page.url.pathname === "/methodology"}><a href="/methodology">Methodology</a></li>
				<li class:active={innerWidth > tw_fullnav && $page.url.pathname === "/resources"}><a href="/resources">Resources</a></li>
				<li class:active={innerWidth > tw_fullnav && $page.url.pathname === "/about"}><a href="/about">About Us</a></li>
				<li class:active={innerWidth > tw_fullnav && $page.url.pathname === "/partners"}><a href="/partners">Our Partners</a></li>
				<li class:active={innerWidth > tw_fullnav && $page.url.pathname === "/contact"}><a href="/contact">Contact Us</a></li>
			</ul>
		</nav>
	</div>
</header>

<style>
	.logo img { filter: invert() brightness(85%) sepia(20%) hue-rotate(120deg); }
	:checked ~ .toggle-mobile-menu .hamburger { display: none; }
	:checked ~ .toggle-mobile-menu .cross { display: flex; }
	:checked ~ nav { display: block; }
	nav li { padding: 0.25rem 1rem; }
	.active { border-bottom: 2px solid theme('colors.brand-primary-dark-green'); font-weight: theme('fontWeight.bold'); }
</style>
