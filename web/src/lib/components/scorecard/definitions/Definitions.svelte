<script type="ts">
	import { access, indicators, proficiency } from '../../../domain/Indicator';
	import Definition from './Definition.svelte';
</script>

<div class="grid grid-cols-1 sm:grid-cols-3 gap-8 gap-y-8">
	<p class="sm:col-span-4 pt-0">
		We believe Access, Proficiency and Excellence are key components of the overall Equity goal.
		Each component’s Equity score is based on 1 – 4 underlying metrics and uses the same methodology
		as the overall Equity Index score.
	</p>

	{#each indicators as indicator, i}
		<div class="col-span-1">
			<Definition {indicator}>
				{#if indicator === access}
					How much access do Black and Latino communities have to the resources and opportunities
					necessary to succeed on Computer Science pathways?
				{:else if indicator === proficiency}
					How well are we preparing Black and Latino students to pursue and succeed on Computer
					Science pathways?
				{:else}
					How well are we preparing Black and Latino students to succeed at elite levels on Computer
					Science pathways?
				{/if}
			</Definition>
		</div>
	{/each}
</div>
