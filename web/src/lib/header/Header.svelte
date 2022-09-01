<script lang="ts">
	import { page } from '$app/stores';
	// import Nav from './Nav.svelte'
</script>

<header class="w-full items-center border-b border-brand-primary-green z-10">
	<div class="flex justify-between lg:justify-start mx-auto max-w-7xl">
		<input type="checkbox" id="open-mobile-menu" class="hidden" />
		<label for="open-mobile-menu" class="lg:hidden toggle-mobile-menu flex items-center justify-center p-2" aria-controls="mobile-menu" aria-expanded="false">
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
		
		<div class="flex lg:hidden h-10 w-10"><div> </div></div>

		<nav class="hidden lg:flex w-full lg:w-auto absolute lg:static top-12 left-0 right-0 bottom-0 bg-brand-primary-really-light-green p-4 lg:p-0 leading-10 border-t lg:border-0 border-brand-primary-green">
			<ul class="lg:flex">
				<li><a href="/">The Data</a></li>
				<li><a href="/methodology">Methodology</a></li>
				<li><a href="/resources">Resources</a></li>
				<li><a href="/about">About Us</a></li>
				<li><a href="/partners">Our Partners</a></li>
				<li><a href="/contact">Contact Us</a></li>
			</ul>
		</nav>
	</div>
</header>

<style>
	.logo img { filter: invert() brightness(57.5%) sepia(100%) hue-rotate(120deg); }
	:checked ~ .toggle-mobile-menu .hamburger { display: none; }
	:checked ~ .toggle-mobile-menu .cross { display: flex; }
	:checked ~ nav { display: block; }
	nav li { padding: 0.25rem 1rem; }
</style>
