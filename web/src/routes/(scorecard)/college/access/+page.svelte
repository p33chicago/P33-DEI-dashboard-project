<script type="ts">
	import Figure from '$lib/components/figure/Figure.svelte';
	import DataDive from '$lib/components/DataDive.svelte';
	import { college } from '$lib/domain/Lifestage';
</script>

<svelte:head>
	<meta content="Help promote equity in tech." name="description" />
</svelte:head>

<DataDive
	header="Illinois CS/Computing Degree Enrollment"
	subheader="Percent of Illinois college students enrolled into a CS/Computing degree by race/ethnicity"
>
	<svelte:fragment slot="story">
		<p>
			At the Universities in Illinois, Over 67 out of 100 Asian high school graduates chose CS
			major, the ratio is 15 out of 100 for white graduates, 21 out of 100 for Hispanic students,
			and 13 out of 100 for black graduates.
		</p>
	</svelte:fragment>

	<svelte:fragment slot="takeaways">
		<p />
	</svelte:fragment>
	<Figure file={`metrics/${college.route}/cs_enrol`} slot="figure" />
</DataDive>

<DataDive
	header="Illinois Immediate College Enrollment Rates"
	subheader="Percent of Illinois High School graduates that immediately enroll in college by race/ethnicity"
>
	<svelte:fragment slot="story">
		<p />
	</svelte:fragment>

	<svelte:fragment slot="takeaways">
		<p />
	</svelte:fragment>
	<Figure file={`metrics/${college.route}/imdEnrol`} slot="figure" />
</DataDive>
