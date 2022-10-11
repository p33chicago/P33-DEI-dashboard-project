<script type="ts">
	import Figure from '$lib/components/figure/Figure.svelte';
	import DataDive from '$lib/components/DataDive.svelte';
	import { career } from '$lib/domain/Lifestage';
</script>

<DataDive
	header="Chicago MSA tech employee demographics"
	subheader="Proportion of Chicago MSA degree holders working in a top 11 tech occupation"
>
	<svelte:fragment slot="story">
		<p>
			In the Chicago metropolitan region, the number of tech jobs occupied by Asian workers is 10%
			of the total number of Asian college graduates. The ratio is 4% for white and Hispanic
			graduates and 2.5% for black graduates.
		</p>
		<p>
			The ratio of tech job occupations to the number of college graduates in the Metropolitan
			region of the City of Chicago is slightly lower than the national average across all ethnic
			groups.
		</p>
	</svelte:fragment>

	<svelte:fragment slot="takeaways">
		<p>
			Hispanic students have to compete with 100 peer graduates for 4 job opportunities in tech
			companies, Black students have to compete with 100 peer graduates for 2 job opportunities in
			tech companies.
		</p>
	</svelte:fragment>
	<Figure file={`metrics/${career.route}/techJob`} slot="figure" />
</DataDive>
