<script type="ts">
	import Figure from '$lib/figure/Figure.svelte';
	import DataDive from '$lib/DataDive.svelte';
	import { highSchool } from '$lib/domain/Lifestage.ts';
</script>

<DataDive
	header="HS SAT Math Proficiency and Above"
	subheader="Percent of CPS SAT takers at or above math standards by race/ethnicity"
>
	<svelte:fragment slot="story">
		<p>
			Over 50% of White and Asian students meet SAT Math benchmark while no more than 20% of Black
			and Hispanic students meet SAT Math benchmark.
		</p>
		<p>
			Only the White population in CPS high school perform slightly above the national average.
			Asian, Hispanic, and black students have the SAT math benchmark meeting rate 11% - 30% lower
			than the national average.
		</p>
	</svelte:fragment>

	<svelte:fragment slot="takeaways">
		<p>
			Deep disparity in math proficiency rate. The proportion of White and Asian students who meet
			sat math benchmark is 2.7 - 5.6 times higher than that of Hispanic and Black students.
		</p>
	</svelte:fragment>
	<Figure lifestage={highSchool.route} name="sat_meetAndExceeds" slot="figure" />
</DataDive>

<DataDive
	header="AP CS scoring 3 or higher"
	subheader="Percent of CPS AP CS students scoring a 3 or higher by race/ethnicity"
>
	<svelte:fragment slot="story">
		<p>
			The proportion of White students in CPS high school score 3 or higher is nearly 70%, 1.1 times
			higher than Asians, and 2.1 times higher than Hispanic, and 4 times higher than Black.
		</p>
		<p>
			CPS High school students have their proportion of scoring 3 on AP CS lower than the national
			average.
		</p>
	</svelte:fragment>

	<svelte:fragment slot="takeaways">
		<p>
			Deep disparity in AP CS scoring. The proportion of White and Asian students who scores 3 or
			higher in AP CS is 1.9 - 4 times higher than that of Hispanic and Black students.
		</p>
	</svelte:fragment>
	<Figure lifestage={highSchool.route} name="apcs_aboveThree" slot="figure" />
</DataDive>
