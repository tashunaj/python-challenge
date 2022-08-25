import csv
in_file = "data/election_data.csv"
out_file= "analysis/election_data.txt"


total_votes = 0

candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0


with open(in_file) as election_data:
    reader = csv.DictReader(election_data)


    
    for row in reader:
        
   
        total_votes = total_votes + 1
        candidate_name = row["Candidate"]
        
        if candidate_name  not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name]= candidate_votes[candidate_name] + 1

with open(out_file, 'w') as txt_file: 

    results_of_election = (
        f"\n\nElection Results\n"
        f"----------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n"
    )

    print(results_of_election)
    txt_file.write(results_of_election)

    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        vote_percent = float(votes) / float(total_votes) *100

        if(votes > winning_count):
            winning_count = votes
            winning_candidate = candidate
        voter_out = f"{candidate}: {vote_percent:3f}% ({votes})\n"
        print(voter_out)

        txt_file.write(voter_out)

    winning_summary = (
        f"--------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-----------------------\n"
        )
    print(winning_summary)

    txt_file.write(winning_summary)
