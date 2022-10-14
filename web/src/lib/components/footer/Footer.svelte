<script>
	import { assets, base } from '$app/paths';
	import HorizontalNav from '$lib/components/horizontal_nav/HorizontalNav.svelte';
	import HorizontalNavItem from '$lib/components/horizontal_nav/HorizontalNavItem.svelte';
	import { default_scorecard_path } from '$lib/pathnames';

	const year = new Date().getFullYear();
</script>

<!--<div class="flex grow" />-->
<div class="w-full bg-black">
	<footer
		class="text-sm sm:text-base px-4 xl:px-12 flex flex-col xl:flex-row text-white py-9 gap-x-10 gap-y-8 text-center xl:text-left font-sans-alternate uppercase"
	>
		<p class="grow justify-center xl:justify-self-start">
			<HorizontalNav class="nav">
				<HorizontalNavItem href={base}>Home</HorizontalNavItem>
				<HorizontalNavItem href="{base}/{default_scorecard_path}">Scorecard</HorizontalNavItem>
				<HorizontalNavItem href="{base}/solutions">Solutions</HorizontalNavItem>
				<HorizontalNavItem href="{base}/about">About</HorizontalNavItem>
				<HorizontalNavItem href="{base}/contact">Contact</HorizontalNavItem>
			</HorizontalNav>
		</p>
		<p>
			<HorizontalNav class="details">
				<HorizontalNavItem>
					&copy; {year}
				</HorizontalNavItem>
				<HorizontalNavItem
					class="text-white"
					href="https://p33chicago.com/privacy-policy"
					target="_blank"
				>
					Privacy Policy
				</HorizontalNavItem>
				<HorizontalNavItem class="partnership">
					In partnership with
					<img
						alt="Thoughtworks"
						class="inline-block h-[24px] pb-[3px]"
						height="24"
						src="{assets}/thoughtworks-light.svg"
					/>
				</HorizontalNavItem>
			</HorizontalNav>
		</p>
		<div class="xl:justify-self-end xl:self-center space-x-4">
			<a alt="linkedin" href="https://www.linkedin.com/company/p33-chicago/" target="_blank">
				<img class="inline-block" height="24" src="{assets}/linkedin.svg" width="24" />
			</a>
			<a alt="twitter" href="https://twitter.com/P33Chicago" target="_blank">
				<img class="inline-block" height="24" src="{assets}/twitter.svg" width="24" />
			</a>
		</div>
	</footer>
</div>

<style>
	/** -- vertical separators */
	:global(.nav) > :global(li):not(:first-child)::before,
	:global(.details) > :global(li):not(:first-child)::before {
		content: '';
		display: inline-block;
		width: 1px;
		height: 1em;
		position: relative;
		background-color: theme('colors.really-light-gray');
		top: 0.1em;
	}
	@media screen(xl) {
		:global(.nav) > :global(li):not(:first-child)::before {
			display: none !important;
		}
	}

	/** -- special style for separator before "In partnership with ..." */
	:global(.partnership)::before {
		display: none !important;
	}
	@media screen(sm) {
		:global(.partnership)::before {
			display: inline-block !important;
		}
	}
</style>
