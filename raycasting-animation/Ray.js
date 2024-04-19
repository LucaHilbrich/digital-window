class Ray
{
    constructor(id, viewer, ray_anchor, projection_surface)
    {
        this.id = id;
        this.viewer = viewer;
        this.ray_anchor = ray_anchor;
        this.projection_surface = projection_surface;
        this.projected_point = false;
    }

    run()
    {
        this.update();
        this.display();
        this.log();
    }

    update()
    {
        let v = createVector(
            (this.ray_anchor.pos.x - this.viewer.pos.x) * 100,
            (this.ray_anchor.pos.y - this.viewer.pos.y) * 100
        );
        for (let b of this.projection_surface.boundaries)
        {
            if (b.is_intersecting(v.x, v.y, this.ray_anchor.pos.x, this.ray_anchor.pos.y))
            {
                this.projected_point = b.intersection;
            }
        }
    }

    log()
    {
        console.log(
            this.id,
            (atan(this.projected_point.y / this.projected_point.x) + PI/2) / PI * 180
        );
    }

    display()
    {
        noFill();
        stroke(255);
        line(this.viewer.pos.x, this.viewer.pos.y, this.ray_anchor.pos.x, this.ray_anchor.pos.y);
        line(this.viewer.pos.x, this.viewer.pos.y, this.projected_point.x, this.projected_point.y);
        if (this.projected_point)
        {
            circle(this.projected_point.x, this.projected_point.y, 20);
        }
    }
}