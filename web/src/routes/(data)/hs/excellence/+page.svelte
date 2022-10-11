<script type="ts">
	import Figure from '$lib/components/figure/Figure.svelte';
	import DataDive from '$lib/components/DataDive.svelte';
	import { highSchool } from '$lib/domain/Lifestage';
</script>

<DataDive
	header="HS SAT Math Advanced"
	subheader="Percent of CPS SAT takers advancing math standards by race/ethnicity"
>
	<svelte:fragment slot="story">
		<p>No more than 2% of Hispanic students and 1% of Black students advance in SAT math tests.</p>
		<p>
			CPS High school students have a proportion of SAT math advanced students significantly lower
			than the national average across all ethnic groups.
		</p>
	</svelte:fragment>

	<svelte:fragment slot="takeaways">
		<p>
			Extreme disparity in sat math advance rate. The proportion of White and Asian students who
			advance SAT math is 12.3 - 34 times higher than that of Hispanic and Black students in CPS.
		</p>
	</svelte:fragment>
	<Figure file={`metrics/${highSchool.route}/sat_exceeds`} slot="figure" />
</DataDive>

<DataDive
	header="CPS AP CS scored 5"
	subheader="Percent of CPS AP CS students scoring a 5 by race/ethnicity"
>
	<svelte:fragment slot="story">
		<p>No more than 3% of Hispanic students and 2% of Black students scored 5 on AP CS.</p>
		<p>
			White students in CPS high school perform noticeably better than the national average.
			However, Asian, Hispanic, and black students all have a high AP CS scoring rate below the
			national average.
		</p>
	</svelte:fragment>

	<svelte:fragment slot="takeaways">
		<p>
			Extreme disparity in AP CS high scoring rate. The proportion of White and Asian students who
			score 5 on AP CS is 6 - 17 times higher than that of Hispanic and Black students in CPS.
		</p>
	</svelte:fragment>
	<Figure file={`metrics/${highSchool.route}/apcs_five`} slot="figure" />
</DataDive>
