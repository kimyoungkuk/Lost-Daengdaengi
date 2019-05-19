import Main_ from '../components/Main' 
import Login_ from '../components/Login'
import Map_ from '../components/Map' 
import Board_ from '../components/Board'
import makePost_ from '../components/makePost'
import imgPick_ from '../components/imgPick'
import camera_ from '../components/camera'
import SetUserInfo_ from '../components/SetUserInfo'
import gps_ from '../components/gps'
import select_Loc_ from '../components/select_Loc'
import makePost_Finder_ from '../components/makePost_Finder'
const router = { 
   main: Main_, 
   login: Login_,
   map: Map_,
   board: Board_,
   camera : camera_,
   gps : gps_,
  // boardWrite: Board_Write,
   setUserInfo: SetUserInfo_,
   makePost : makePost_,
   select_Loc : select_Loc_,
   imgPick : imgPick_,
   makePost_Finder :makePost_Finder_
}
export default router