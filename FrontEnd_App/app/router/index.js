import Main_ from '../components/Main' 
import Login_ from '../components/Login'
import Map_ from '../components/Map' 
import Board_ from '../components/Board'
import makePost_ from '../components/makePost'
import Board_Write from '../components/BoardWrite'
import camera_ from '../components/camera'
import SetUserInfo_ from '../components/SetUserInfo'

const router = { 
   main: Main_, 
   login: Login_,
   map: Map_,
   board: Board_,
   camera : camera_
   boardWrite: Board_Write,
   setUserInfo: SetUserInfo_,
  // makePost : makePost_,
}
export default router