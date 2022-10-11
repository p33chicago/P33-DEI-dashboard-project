<script type="ts">
	import Figure from '$lib/components/figure/Figure.svelte';
	import DataDive from '$lib/components/DataDive.svelte';
	import { highSchool } from '$lib/domain/Lifestage.ts';
</script>

<DataDive header="AP CS Enrollment" subheader="Percent of CPS HS students enrolled in AP CS">
	<svelte:fragment slot="story">
		<p>
			Asian students have the highest AP CS enrollment rate of 8%. 1.2 times higher than White, 4
			times higher than Hispanics, and 7 times higher than black.
		</p>
		<p>
			AP CS enrollment rate of students in CPS is significantly higher than the national average.
			The proportion of White students enroll to AP CS is 6 times higher than the national average.
		</p>
	</svelte:fragment>
	<svelte:fragment slot="takeaways">
		<p>
			CPS has an overall much higher AP CS enrolment rate in comparison with the national average
			across all ethnic groups. However, the disparity is enormous, White and Asian students have an
			enrollment rate 3-7 times higher than Black and Hispanic students.
		</p>
	</svelte:fragment>
	<Figure file={`metrics/${highSchool.route}/apcs_enrol`} slot="figure" />
</DataDive>

<DataDive
	header="CPS HS STEM Magnet School Enrollment"
	subheader="Percent of CPS HS students enrolled in a STEM magnet school by race/ethnicity"
>
	<svelte:fragment slot="story">
		<p>
			Asian students have the highest AP CS enrollment rate of 8%. 1.2 times higher than White, 4
			times higher than Hispanics, and 7 times higher than black.
		</p>
	</svelte:fragment>
	<svelte:fragment slot="takeaways">
		<p>
			13.25% of Black students enrolled in STEM Magnet elementary schools while only 8.82% enrolled
			in STEM Magnet high school.
		</p>
		<p>
			7.87% of Hispanic students enrolled in STEM Magnet elementary schools while 19.66% enrolled in
			STEM Magnet high school.
		</p>
	</svelte:fragment>
	<Figure file={`metrics/${highSchool.route}/magnet_enrol`} slot="figure" />
</DataDive>

<DataDive
	header="CS Interest"
	subheader="Percent of CPS HS students indicating interest in an CS/IT career"
>
	<svelte:fragment slot="takeaways">
		<p>
			1 out of 4 Asian students express an interest in Computer Science, in comparison with 1 out of
			5 white students, 1 out of 10 Hispanic students, and 1 out of 20 black students expressing the
			same interest.
		</p>
	</svelte:fragment>
	<Figure file={`metrics/${highSchool.route}/CSInterested`} slot="figure" />
</DataDive>

<DataDive
	header="Advanced Math Enrollment"
	subheader="Percent of CPS SAT takers exceeding standards by race/ethnicity"
>
	<svelte:fragment slot="story">
		<p>
			In Chicago, almost 4 out of 10 White and Asian students in CPS enrolled in advanced math
			class, 3 out of 10 Black and Hispanic students enrolled in advanced math class.
		</p>
		<p>
			Overall, the proportion of students who enrolled in advanced math classes in CPS is twice the
			proportion in the national average.
		</p>
	</svelte:fragment>

	<svelte:fragment slot="takeaways">
		<p>
			Minor racial disparity detected in advanced math enrollment rate. Superior performances of CPS
			in related to the national average.
		</p>
	</svelte:fragment>
	<Figure file={`metrics/${highSchool.route}/advMath_enrol`} slot="figure" />
</DataDive>
