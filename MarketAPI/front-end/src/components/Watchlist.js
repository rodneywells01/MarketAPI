import React from 'react';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';

class Watchlist extends React.Component {
    // constructor(props) {
    //     // Display
    // }

    render() {
        return (
            <div>
                <h1>This is your Watchlist</h1>
                <Card>
                    <CardContent>TSLA</CardContent>
                </Card>
            </div>
        )
    }
}

export default Watchlist


// function SimpleCard(props) {
//     const { classes } = props;
//     const bull = <span className={classes.bullet}>•</span>;

//     return (
//       <Card className={classes.card}>
//         <CardContent>
//           <Typography className={classes.title} color="textSecondary" gutterBottom>
//             Word of the Day
//           </Typography>
//           <Typography variant="h5" component="h2">
//             be
//             {bull}
//             nev
//             {bull}o{bull}
//             lent
//           </Typography>
//           <Typography className={classes.pos} color="textSecondary">
//             adjective
//           </Typography>
//           <Typography component="p">
//             well meaning and kindly.
//             <br />
//             {'"a benevolent smile"'}
//           </Typography>
//         </CardContent>
//         <CardActions>
//           <Button size="small">Learn More</Button>
//         </CardActions>
//       </Card>
//     );
//   }

//   SimpleCard.propTypes = {
//     classes: PropTypes.object.isRequired,
//   };

//   export default withStyles(styles)(SimpleCard);