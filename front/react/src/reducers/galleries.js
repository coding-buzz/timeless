import { FETCH_GALLERIES, FETCH_GALLERY, CLEAR_GALLERY } from '../actions/const';


let defaultState = {
  galleries: [],
  activeGallery: null
};


export default (state = defaultState, action) => {
  switch (action.type) {
    case FETCH_GALLERIES:
      return Object.assign({}, state, {galleries: action.galleries});
    case FETCH_GALLERY:
      return Object.assign({}, state, {activeGallery: action.gallery});
    case CLEAR_GALLERY:
      return Object.assign({}, state, {activeGallery: null});
    default:
      return state;
  }
};
