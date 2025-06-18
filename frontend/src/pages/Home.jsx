import React, { useRef, useState } from 'react';
import Spinner from '../animations/Spinner';
import Hole from '../animations/Hole';
import Container from '../animations/Container';
import Goggel from '../animations/Goggle';
import { Mic, Truck, Check} from 'react-feather';
import axios from 'axios'

const Home = () => {
  const [isRecording , setIsRecording] = useState(false)
  const [audioBlob , setAudioBlob] = useState(null)
  const [isGettingAnswer,setIsGettingAnswer] = useState(false)
  const [isAnswering,setIsAnswering] = useState(false)
  const [askedQuestion, setAskedQuestion] = useState("")
  const mediaRecorderRef = useRef()
  const audioRef = useRef()
  const backendApi = import.meta.env.VITE_BACKEND_API
  // const [isQuestioning,setIsQuestioning] = useState(false)
  const [answerAudioURL,setAnswerAudioURL] = useState(null)
  // console.log(backendApi);
  

  const handleStartRecording = async ()=>{
    try {
      console.log("started recording");
    const stream = await navigator.mediaDevices.getUserMedia({audio:true});
    const mediaRecorder = new MediaRecorder(stream);
    mediaRecorderRef.current = mediaRecorder

    const audioChunks =[]
    mediaRecorder.ondataavailable = (e)=>{
      // console.log(e.data.size);
      if(e.data.size >10){
        console.log("yes");
        
      }
      else{
        console.log("10");
        
      }
      audioChunks.push(e.data)
    }
    mediaRecorder.onstop = ()=>{
      console.log(audioChunks);
      
      const audioBlobs = new Blob(audioChunks, {type: "audio/wav"});
      setAudioBlob(audioBlobs)
      handleAskQuestion(audioBlobs)
    }

    mediaRecorder.start()
    setIsRecording(true)
    setAudioBlob(null)
    setAnswerAudioURL(null)
      
    } catch (error) {
      console.log(error);
      if(error == "NotAllowedError: Permission denied"){
        alert("Please give permission to continue")
        navigator.mediaDevices && navigator.mediaDevices.getUserMedia
      }
      
    }
    

  }

  const handleStopRecording = ()=>{
    if(mediaRecorderRef.current){
      mediaRecorderRef.current.stop()
      setIsRecording(false)
    }
  }

  const handleAskQuestion = async (audioBlobs)=>{
    if(!audioBlobs){
      console.log("No audio to send");
      alert("audio is not clear")
      return
    }
    try {
      setIsGettingAnswer(true)
      const formData = new FormData()
      formData.append("audio",audioBlobs,"recording.wav");

      const resp = await axios.post(`${backendApi}/talk`,formData,
        {
          headers : {"Content-Type" : "multipart/form-data"},
          responseType : "blob"
        }
      )

      setAskedQuestion(resp.headers["asked_question"]);
      console.log(resp);
      
      const audioURL = URL.createObjectURL(resp.data)
      setAnswerAudioURL(audioURL)
      setIsGettingAnswer(false)
    } catch (error) {
        console.log(error.message);
        
    }
    
  }

  return (
    <div className=" h-screen bg-white text-black w-screen flex items-center justify-center">
      <div className='w-[90%] h-[90%] text-center flex flex-col items-center justify-evenly'>
        <div className='text-5xl font-italic font-semibold'>
          <span className='text-green-600 font-extrabold '>Sriram </span>
          Voice Assistant
        </div>
        <div className='border card green-shadow h-[77%] w-[77%] flex flex-col justify-end gap-10 items-center'>
          <button  className='lg:mb-7 sm:mb-2 '>
            {
              isRecording? <Goggel/> : isGettingAnswer? <Hole/> : 
              answerAudioURL? 
              <>
              <Spinner/>
              <audio controls onEnded={()=>{setAnswerAudioURL(null)}}  ref={audioRef} style={{ display: 'none' }}   autoPlay src={answerAudioURL}></audio></> : <Container/>
              
            }
          </button>
          {
            askedQuestion?
            <h1 className='p-2 text-sm bg-slate-300 glass text-gray-500 border border-slate-200 rounded-xl'>{askedQuestion+"?"}</h1> : <h1 className='p-2 text-sm bg-slate-300 glass text-gray-500 border border-slate-200 rounded-xl'>No question yet...</h1>
          }
          <button className={`${!isGettingAnswer?'cursor-pointer':'cursor-not-allowed'}`} disabled={isGettingAnswer} >
            {
              isRecording? <Check className='p-5 rounded-full glass w-full h-full'  onClick={handleStopRecording} /> : <Mic className='p-5 rounded-full glass w-full h-full'  onClick={handleStartRecording} />
            }
          </button>
          <div className='mb-2 flex w-full lg:overflow-hidden  sm:overflow-x-scroll gap-3 items-center lg:justify-evenly sm:justify-start'>
            <h1 className='p-3 min-w-fit bg-slate-300 glass text-gray-500 border border-slate-200 rounded-xl'>What is you experience?</h1>
            <h1 className='p-3 min-w-fit bg-slate-300 glass text-gray-500 border border-slate-200 rounded-xl'>Tell me about your self?</h1>
            <h1 className='p-3 min-w-fit bg-slate-300 glass text-gray-500 border border-slate-200 rounded-xl'>What is your goal?</h1>
            <h1 className='p-3 min-w-fit bg-slate-300 glass text-gray-500 border border-slate-200 rounded-xl'>Where can you see your self in next 5 years?</h1>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Home;
