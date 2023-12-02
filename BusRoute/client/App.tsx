import { List, nil } from './List';

// TODO: interfaces+classes

type coords = {long: number, lat: number}

type BusStop = {
    /** Location of the bus stop, longitude and latitude */
    location: coords;

    /** Recommendation of the bus stop (percentage of time saved) */
    rec: number;
}

/** Generates 10 potential stops for a new bus route */
const generateStops = (center: coords): List<BusStop> => {
    return nil;
}