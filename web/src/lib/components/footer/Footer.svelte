<script>
	import FooterNav from '$lib/components/footer/FooterNav.svelte';
	import { assets } from '$app/paths';

	const year = new Date().getFullYear();
</script>

<div class="flex grow" />
<div class="w-full bg-black">
	<footer
		class="text-sm sm:text-base px-7 lg:px-8 col-span-1 sm:col-span-4 flex flex-col xl:flex-row text-white py-9 gap-x-10 gap-y-6 text-center xl:text-right font-sans-alternate uppercase"
	>
		<p class="grow leading-loose">
			<FooterNav />
		</p>
		<p class="leading-loose">
			<span>&copy; {year}</span>
			<span class="inline-block h-[1rem] mx-2 relative top-[1px] w-[1px] bg-white" />
			<a class="text-white" href="https://p33chicago.com/privacy-policy" target="_blank">
				Privacy Policy
			</a>
			<span class="hidden sm:inline-block h-[1rem] mx-2 relative top-[1px] w-[1px] bg-white" />
			<span class="whitespace-nowrap">
				In partnership with <img
					alt="Thoughtworks"
					class="inline-block h-[24px] pb-[3px]"
					height="24"
					src="{assets}/thoughtworks-light.svg"
				/>
			</span>
		</p>
		<div class="xl:justify-self-end space-x-4">
			<a alt="linkedin" href=""
				><img class="inline-block" height="24" src="{assets}/linkedin.svg" width="24" /></a
			>
			<a alt="twitter" href=""
				><img class="inline-block" height="24" src="{assets}/twitter.svg" width="24" /></a
			>
		</div>
	</footer>
</div>
