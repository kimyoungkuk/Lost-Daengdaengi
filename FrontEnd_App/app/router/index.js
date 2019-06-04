import Main_ from '../components/Main' 
import Login_ from '../components/Login'
import Map_ from '../components/Map' 
import makePost_ from '../components/makePost'
import imgPick_ from '../components/imgPick'
import camera_ from '../components/camera'
import SetUserInfo_ from '../components/SetUserInfo'
import FinderBoard_ from '../components/FinderBoard'
import OwnerBoard_ from '../components/OwnerBoard'
import select_Loc_ from '../components/select_Loc'
import makePost_Finder_ from '../components/makePost_Finder'
import Mypage_ from '../components/mypage'
import makeFinderPost_ from '../components/makeFinderPost'
import makeFinderPostWeb_ from '../components/makeFinderPostWeb'
import makeOwnerPost_ from '../components/makeOwnerPost'
import makeOwnerPostWeb_ from '../components/makeOwnerPostWeb'
import googlemap_t_ from '../components/googlemap_t'

const router = { 
   mypage : Mypage_,
   main: Main_, 
   login: Login_,
   map: Map_,
   camera : camera_,
   setUserInfo: SetUserInfo_,
   makePost : makePost_,
   finderBoard: FinderBoard_,
   select_Loc : select_Loc_,
   imgPick : imgPick_,
   makePost_Finder :makePost_Finder_,
   ownerBoard: OwnerBoard_,
   makeFinderPost: makeFinderPost_,
   makeFinderPostWeb: makeFinderPostWeb_,
   makeOwnerPost: makeOwnerPost_,
   makeOwnerPostWeb: makeOwnerPostWeb_,
   googlemap_t : googlemap_t_
}
export default router