class ProjectionSurface
{
    constructor(radius, n_boundaries)
    {
        this.radius = radius;
        this.boundaries = [];
        let angle = -PI/2;
        let x1 = radius * cos(angle);
        let y1 = radius * sin(angle);
        for (let i = 0; i < n_boundaries; i++)
        {
            angle += PI/n_boundaries;
            let x2 = radius * cos(angle);
            let y2 = radius * sin(angle);
            this.boundaries.push(
                new Boundary(x1, y1, x2, y2)
            );
            x1 = x2;
            y1 = y2;
        }
    }

    display()
    {
        noFill();
        stroke(255, 0, 0);
        for (let b of this.boundaries)
        {
            b.display();
        }
    }
}