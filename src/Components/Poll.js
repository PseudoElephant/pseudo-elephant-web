import React,{useState} from 'react'
import Poll from  "react-polls";



export default function CustomPoll(){
// Declaring poll question and answers
const pollQuestion = 'Codein Challenge?';
 const pollAnswers = [
    { option: 'Yes', votes: 8 },
    { option: 'No', votes: 4},
    {option: 'Anal',votes:25 }
]
const [answers,setAnswers] = useState(pollAnswers);

function handleVote(vote) {
    const new_answers = answers.map(
      answer => {
          if (answer.option === vote) answer.votes++
          return answer
      }
    );
    setAnswers(new_answers);
  }

return (
    <div>
    <div className="containing">
            <Poll className="meg" question={pollQuestion} answers={answers} onVote={(val) => handleVote(val)} theme="purple" questionColor="#303030"
            align="center" noStorage questionSeparator={true} style={{"color":"purple", "background":"white","font-size":"10rem"}}
/>
    </div>
    <div className="containing">
        <Poll className="meg" question={pollQuestion} answers={answers} onVote={voteAnswer => handleVote(voteAnswer)} theme="purple" questionColor="#303030"
            align="center" noStorage questionSeparator={true} style={{ "color": "purple", "background": "white", "font-size": "10rem" }}
        />
    </div>
    <div className="containing">
        <Poll className="meg" question={pollQuestion} answers={answers} onVote={voteAnswer => handleVote(voteAnswer)} theme="purple" questionColor="#303030"
            align="center" noStorage questionSeparator={true} style={{ "color": "purple", "background": "white", "font-size": "10rem" }}
        />
    </div>
    </div>
)
}
