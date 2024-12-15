from api.job_search import search_for_jobs, job_details


def filtered_jobs(keywords, location, resume_skills):
    jobs = search_for_jobs(keywords, location)
    matched_jobs = []
    set1 = set(s.lower() for s in resume_skills)
    # print(len(jobs))
    # if len(jobs) > 3:
    #     jobs = jobs[:5]
    for job in jobs:
        job_detail = job_details(job[0]["id"])
        set2 = set(s.lower() for s in job_detail)
        similar_skills = set1.intersection(set2)

        # print(similar_skills)
        if len(similar_skills) >= 1:
            matched_jobs.append(job)

    # print(f"{len(matched_jobs)} job(s) found: \n {matched_jobs}")
    return matched_jobs


# res_skills = [
#     "Node.js",
#     "TypeScript",
#     "NestJS",
#     "Next.js",
#     "Java",
#     "Python",
#     "HTML",
#     "CSS",
# ]


# cached_res = filtered_jobs(key_words_list, "Chicago", tuple(res_skills))
# print(cached_res)
