<script>
	import SocialButtons from './SocialButtons.svelte';

	export let header;
	export let subheader;
</script>

<div class="mx-3 grid grid-cols-1 sm:grid-cols-2 gap-4 border-b-[1px] border-light-gray">
	<div class="grid col-span-2 pt-9">
		<h2>{header}</h2>
	</div>
	<div class="col-span-1">
		<h4>What does the data tell?</h4>
		<div class="space-y-6">
			<slot name="story" />
		</div>

		<h4 class="mt-6">Takeaways</h4>
		<div class="space-y-6">
			<slot name="takeaways" />
		</div>
	</div>
	<div class="flex flex-col col-span-1 -order-1 sm:order-none">
		<slot name="figure" />
		<p>{subheader}</p>
	</div>
	<SocialButtons />
</div>
