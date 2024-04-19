const WIN_WIDTH = 50;
const PROJECTION_SURFACE_RADIUS = 200;
let TRANSLATE_X, TRANSLATE_Y;
let viewer;
let ray_anchors = [];
let projection_surface;
let rays = [];

function setup()
{
    createCanvas(1200, 400);
    viewer = new Viewer();
    ray_anchors.push(
        new RayAnchor(0, -WIN_WIDTH/2),
        new RayAnchor(0, WIN_WIDTH/2)
    )
    projection_surface = new ProjectionSurface(PROJECTION_SURFACE_RADIUS - 20, 64);
    rays.push(
        new Ray("left:", viewer, ray_anchors[0], projection_surface),
        new Ray("right:", viewer, ray_anchors[1], projection_surface)
    );
}

function draw()
{
    background(35);
    TRANSLATE_X = width - PROJECTION_SURFACE_RADIUS - 20;
    TRANSLATE_Y = height/2;
    translate(TRANSLATE_X, TRANSLATE_Y);
    draw_walls();
    viewer.run();
    for (let r of ray_anchors)
    {
        r.display();
    }
    projection_surface.display();
    
    for (let r of rays)
    {
        r.run();
    }
}

function draw_walls()
{
    stroke(180);
    line(0, -width/2, ray_anchors[0].pos.x, ray_anchors[0].pos.y);
    line(0, width/2, ray_anchors[1].pos.x, ray_anchors[1].pos.y);
}